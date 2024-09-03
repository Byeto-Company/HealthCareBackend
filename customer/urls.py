from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'customer'
urlpatterns = [
    path('get-cities/', views.get_cities, name='get_cities'),

]

router = DefaultRouter()
router.register(r'customer', views.CustomerViewSet, basename='customer')
router.register(r'province', views.CustomerProvinceViewSet, basename='province')

urlpatterns += router.urls
