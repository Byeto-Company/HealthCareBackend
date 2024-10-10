from unicodedata import category

from rest_framework import serializers
from .models import *

class CategoryBreadcrumbSerializer(serializers.ModelSerializer):
    breadcrumb = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'breadcrumb']

    def get_breadcrumb(self, obj):
        full_path = [
            obj.name,
        ]
        parent = obj.parent
        while parent is not None:
            full_path.append(f"parent_name: {parent.name},"
                             f"parent_slug: {parent.slug},")
            parent = parent.parent
        return ', '.join(full_path[::-1])




class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['feature_text']

    def to_representation(self, instance):
        return instance.feature_text

class CapabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Capability
        fields = ['detail_text']

    def to_representation(self, instance):
        return instance.detail_text

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ['id', 'image', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = CategoryBreadcrumbSerializer()
    slides_list = SlideSerializer(many=True, read_only=True, source='slides')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'product_icon_photo', 'slug', 'slides_list']

class ProductSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'product_icon_photo', 'slug']

class CategoriesSerializer(serializers.ModelSerializer):
    product_list = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'product_list']
    def get_product_list(self, obj):
        product = Product.objects.filter(category=obj.id)
        return ProductSerializer1(product, many=True).data

class ProductCategoriesSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent']

    def get_parent(self, obj):
        # Avoid deep recursion by limiting the depth to one level of parent
        if obj.parent:
            return {'id': obj.parent.id, 'name': obj.parent.name, 'slug': obj.parent.slug}
        return None

class ProductDetailSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    features_list = FeatureSerializer(many=True, read_only=True, source='features')
    capability_list = CapabilitySerializer(many=True, read_only=True, source='capability')
    category = ProductCategoriesSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'category', 'thumbnail', 'features_list', 'capability_list',
                  'categories']

    def get_categories(self, obj):
        categories = Category.objects.all()
        return CategoriesSerializer(categories, many=True).data

