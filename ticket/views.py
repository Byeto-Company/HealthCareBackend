from rest_framework import viewsets
from .models import RequestDemo, ContactUs
from .serializers import RequestDemoSerializer, ContactUsSerializer


class RequestDemoViewSet(viewsets.ModelViewSet):
    queryset = RequestDemo.objects.all()
    serializer_class = RequestDemoSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
