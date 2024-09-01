from .serializer import CustomerSerializer
from .models import Customer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse
from .models import City


class CustomerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    partial_update = None


def get_cities(request):
    province_id = request.GET.get('province')
    cities = City.objects.filter(province_id=province_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)
