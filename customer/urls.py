from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'customer'
urlpatterns = [
    path('cities', views.GetCityView.as_view()),
    path('province', views.GetProvinceView.as_view()),
    path('customer', views.CustomerGetView.as_view()),
    path('create', views.CustomerCreateView.as_view())
]

router = DefaultRouter()
# router.register(r'customer', views.CustomerViewSet, basename='customer')
router.register(r'province', views.CustomerProvinceViewSet, basename='province')

urlpatterns += router.urls
