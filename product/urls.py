from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'Product'
urlpatterns = [
    path('detail/<str:slug>', views.ProductDetailView.as_view()),
    path('list', views.ProductListView.as_view()),
]

# router = DefaultRouter()
# router.register(r'categories', views.CategoryViewSet, basename='category')
# router.register(r'', views.ProductViewSet, basename='product')
# urlpatterns += router.urls

