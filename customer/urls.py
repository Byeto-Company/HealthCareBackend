from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'customer'
urlpatterns = [
]

router = DefaultRouter()
router.register(r'viewset', views.CustomerViewSet, basename='customer')
urlpatterns += router.urls