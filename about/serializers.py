from rest_framework import serializers
from .models import WorkTags, WorkField, Manager, Certificate, Soical


class WorkFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkField
        fields = '__all__'
        read_only_fields = [id, ]


class WorkTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTags
        fields = '__all__'
        read_only_fields = [id, ]


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
        read_only_fields = [id, ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
        read_only_fields = [id, ]


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soical 
        fields = '__all__'
        read_only_fields = (id, )
