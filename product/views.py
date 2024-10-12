from unicodedata import category

from .serializers import *
from .models import Product, Category
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .pagination import ProductLimitOffsetPagination
from rest_framework.views import APIView, Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.shortcuts import get_object_or_404

# class CategoryViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Category.objects.all()
#     serializer_class = CategoryBreadcrumbSerializer
#     partial_update = None


# class ProductViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class = ProductLimitOffsetPagination
#     partial_update = None


class ProductDetailView(APIView):
    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)

        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

class ProductListView(APIView):
    serializer_class = ProductSerializer
    pagination_class = ProductLimitOffsetPagination
    @extend_schema(
        parameters=[
            OpenApiParameter(name='limit', type=int, location=OpenApiParameter.QUERY, description='Number of items per page'),
            OpenApiParameter(name='offset', type=int, location=OpenApiParameter.QUERY, description='Starting position of items'),
        ],
        responses={200: ProductSerializer(many=True)},
    )
    def get(self, request):
        queryset = Product.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)

