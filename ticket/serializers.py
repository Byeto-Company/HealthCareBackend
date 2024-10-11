from rest_framework import serializers
from .models import RequestDemo, ContactUs


class RequestDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDemo
        fields = ['id', 'full_name', 'email', 'phone_number', 'company_name', 'module_name', 'message', 'requested_at']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'full_name', 'email', 'subject', 'message', 'contacted_at']