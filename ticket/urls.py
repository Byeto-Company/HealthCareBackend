from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views



urlpatterns = [
]

router = DefaultRouter()
router.register(r'request-demo', views.RequestDemoViewSet, basename='request-demo')
router.register(r'contact-us', views.ContactUsViewSet, basename='contact-us')

urlpatterns += router.urls