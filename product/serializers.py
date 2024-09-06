from rest_framework import serializers
from .models import Product, Category

class CategoryBreadcrumbSerializer(serializers.ModelSerializer):
    breadcrumb = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'breadcrumb']

    def get_breadcrumb(self, obj):
        full_path = [obj.name]
        parent = obj.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' > '.join(full_path[::-1])

class ProductSerializer(serializers.ModelSerializer):
    category = CategoryBreadcrumbSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category']