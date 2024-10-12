from .pagination import CustomerLimitOffsetPagination
from .serializer import CustomerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse
from .models import City
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import Customer
from rest_framework import status


# class CustomerViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     pagination_class = CustomerLimitOffsetPagination
#     partial_update = None

class CustomerGetView(APIView):
    serializer_class = CustomerSerializer
    def get(self, request):
        customers = Customer.objects.all()
        customers_ser = CustomerSerializer(instance=customers, many=True)
        return Response(customers_ser.data, status=status.HTTP_200_OK)


class CustomerCreateView(APIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
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
