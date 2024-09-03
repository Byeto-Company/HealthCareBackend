from . import views
from rest_framework.routers import DefaultRouter

app_name = 'Product'
urlpatterns = [
]

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'', views.ProductViewSet, basename='product')
urlpatterns += router.urls