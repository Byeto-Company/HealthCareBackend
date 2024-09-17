from rest_framework import serializers
from .models import *

class WorkTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTags
        fields = '__all__'
        read_only_fields = [id, ]


class WorkFieldSerializer(serializers.ModelSerializer):
    work_tags = WorkTagSerializer(many=True, read_only=True)
    class Meta:
        model = WorkField
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


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailModel 
        fields = '__all__'
        read_only_fields = (id, )


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberModel 
        fields = '__all__'
        read_only_fields = (id, )