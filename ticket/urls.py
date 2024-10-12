from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views



urlpatterns = [
    path('request-demo', views.RequestDemoAPIView.as_view(), name='request-demo'),
    path('contact-us', views.ContactUsAPIView.as_view(), name='contact-us'),
]