from rest_framework import serializers
from .models import Customer, Province, City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'name')



class CustomerSerializer(serializers.ModelSerializer):

    city = serializers.SlugRelatedField(slug_field='name', queryset=City.objects.all(), allow_null=True)
    province = serializers.SlugRelatedField(slug_field='name', queryset=Province.objects.all(), allow_null=True)
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['id', ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['corporate_date'] = instance.persian_corporate_date()
        return ret

class CustomerProvinceSerializer(serializers.ModelSerializer):
    customer_count = serializers.IntegerField()

    class Meta:
        model = Province
        fields = ['id', 'name','customer_count']