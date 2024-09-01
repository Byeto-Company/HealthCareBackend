from .serializer import CustomerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse
from .models import City
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import Customer


class CustomerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    partial_update = None


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
