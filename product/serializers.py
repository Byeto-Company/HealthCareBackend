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

class ProductSerializer(serializers.ModelSerializer):
    category = CategoryBreadcrumbSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'product_icon_photo']

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['feature_text']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['detail_text']



class ProductDetailSerializer(serializers.ModelSerializer):
    features_list = FeatureSerializer(many=True, read_only=True, source='features')
    details_list = DetailSerializer(many=True, read_only=True, source='details')
    category = CategoryBreadcrumbSerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'category', 'main_photo', 'secend_photo', 'product_icon_photo', 'features_list', 'details_list']
