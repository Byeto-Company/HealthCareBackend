from rest_framework import serializers
from .models import *

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

class ProductDetailSerializer(serializers.ModelSerializer):
    features_list = FeatureSerializer(many=True, read_only=True, source='features')
    capability_list = CapabilitySerializer(many=True, read_only=True, source='capability')
    category = CategoryBreadcrumbSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'category', 'thumbnail', 'features_list', 'capability_list']
