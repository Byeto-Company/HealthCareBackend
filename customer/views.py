from http.client import responses

from about.models import MetaTagsPage
from .pagination import CustomerLimitOffsetPagination
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse
from .models import City, CustomerTitle
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import Customer, CustomerTitle
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

# class CustomerViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     pagination_class = CustomerLimitOffsetPagination
#     partial_update = None

class CustomerGetView(APIView):
    serializer_class = CustomerSerializer
    pagination_class = CustomerLimitOffsetPagination 
    
    def get(self, request):
        customers = Customer.objects.all()
        paginator = CustomerLimitOffsetPagination()  
        paginated_customers = paginator.paginate_queryset(customers, request)
        metatags = MetaTagsPage.objects.filter(page="customer")
        title = CustomerTitle.objects.first()
        
        customers_ser = CustomerSerializer(instance=paginated_customers, many=True)
        if title:
            return Response({
                "title": title.title,
                "description": title.description,
                "meta": {
                    "title": metatags.first().meta_title,
                    "keywords": metatags.first().meta_keyword,
                    "description": metatags.first().meta_description,
                },
                "customers": paginator.get_paginated_response(customers_ser.data).data,
            })
        else:
            return Response({
                "title": "",
                "description": "",
                "meta": {
                    "keyword": metatags.first().meta_keyword,
                    "description": metatags.first().meta_description,
                },
                "customers": paginator.get_paginated_response(customers_ser.data).data,
            })

class CustomerCreateView(APIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    @extend_schema(
        request=CustomerSerializer,
        responses=CustomerSerializer,
        examples=[
            OpenApiExample(
                'مثال درخواست ساخت مشتری',
                value={
                    "id": 0,
                    "city": "تهران",
                    "province": "تهران",
                    "name": "نام مشتری",
                    "corporate_date": "1401-10-20", 
                    "program_name": "نام محصول"
                },
            ),
            OpenApiExample(
                'مثال پاسخ ساخت مشتری',
                value={
                    "id": 7,
                    "city": "تهران",
                    "province": "تهران",
                    "name": "نام مشتری",
                    "corporate_date": "۱۴۰۱-۱۰-۲۰", 
                    "program_name": "نام محصول"
                },
                response_only=True  
            ),
        ],
    )
    def post(self, request):
        customer_ser = CustomerSerializer(data=request.data)
        if customer_ser.is_valid():
            customer_ser.save()
            return Response(customer_ser.data, status=status.HTTP_201_CREATED)
        return Response(customer_ser.errors, status=status.HTTP_400_BAD_REQUEST)

def get_cities(request):
    province_id = request.GET.get('province')
    cities = City.objects.filter(province_id=province_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)


class GetCityView(APIView):
    serializer_class = CitySerializer
    def get(self, request):
        citys = City.objects.all()
        city_ser = self.serializer_class(instance=citys, many=True)
        return Response(city_ser.data, status=status.HTTP_200_OK)


class GetProvinceView(APIView):
    serializer_class = ProvinceSerializer
    def get(self, request):
        provinces = Province.objects.all()
        provinces_ser = self.serializer_class(instance=provinces, many=True)
        return Response(provinces_ser.data, status=status.HTTP_200_OK)



class CustomerProvinceViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def customer_count_per_province(self, request):
        customer_counts = (
            Customer.objects.values('province__name')
            .annotate(count=Count('id'))
            .order_by('province__name')
        )

        customer_count_dict = {item['province__name']: item['count'] for item in customer_counts}

        return Response(customer_count_dict)
