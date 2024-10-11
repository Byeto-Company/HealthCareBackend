from rest_framework import serializers
from .models import Customer, Province


class CustomerSerializer(serializers.ModelSerializer):
    corporate_date = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['id', ]

    def get_corporate_date(self, obj):
        return obj.persian_corporate_date()

class CustomerProvinceSerializer(serializers.ModelSerializer):
    customer_count = serializers.IntegerField()

    class Meta:
        model = Province
        fields = ['id', 'name','customer_count']