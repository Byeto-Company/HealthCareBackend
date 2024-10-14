from unicodedata import category

from rest_framework import serializers
from .models import *

class CategoryProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'thumbnail')

class CategoryBreadcrumbSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'products',]

    def get_products(self, obj):
        products = Product.objects.filter(category=obj)
        return CategoryProductsSerializer(products, many=True).data


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
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


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

class ProductSerializer(serializers.ModelSerializer):
    meta = serializers.SerializerMethodField()
    category = ProductCategoriesSerializer()
    slides_list = SlideSerializer(many=True, read_only=True, source='slides')
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'product_icon_photo', 'slug', 'slides_list', 'meta']
    def get_categories(self, obj):
        categories = Category.objects.all()
        return CategoriesSerializer(categories, many=True).data

    def get_meta(self, obj):
        data = {
            'meta_keyword': obj.meta_keyword,
            'meta_description': obj.meta_description,
        }
        return data