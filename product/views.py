from .serializers import ProductSerializer, CategoryBreadcrumbSerializer
from .models import Product, Category
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .pagination import ProductLimitOffsetPagination


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategoryBreadcrumbSerializer
    partial_update = None


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductLimitOffsetPagination
    partial_update = None
