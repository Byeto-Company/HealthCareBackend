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


# serializers.py

class HeroLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroLogo
        fields = ['alt', 'link']

class HeroBodyLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroLogo
        fields = ['alt', 'link']

class HeroButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroButton
        fields = ['title', 'link']

class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = ['alt', 'link']

class HeroSerializer(serializers.ModelSerializer):
    buttons = HeroButtonSerializer(many=True)
    images = HeroImageSerializer(many=True)


    class Meta:
        model = Hero
        fields = ['title', 'description', 'buttons', 'images']

class DemoFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoForm
        fields = ['title', 'description']

class DemoSerializer(serializers.ModelSerializer):
    form = DemoFormSerializer()

    class Meta:
        model = Demo
        fields = ['image', 'title', 'subtitle', 'description', 'form']

class AboutProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProject
        fields = ['count', 'title']

class AboutUsSerializer(serializers.ModelSerializer):
    projects = AboutProjectSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = ['image', 'title', 'description', 'projects']

class FooterSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSocial
        fields = ['icon', 'alt', 'link']

class FooterEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterEmail
        fields = ['email']

class FooterPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterPhone
        fields = ['phone']

class FooterSerializer(serializers.ModelSerializer):
    socials = FooterSocialSerializer(many=True)
    emails = FooterEmailSerializer(many=True)
    phones = FooterPhoneSerializer(many=True)

    class Meta:
        model = Footer
        fields = ['title', 'description', 'address', 'socials', 'emails', 'phones', 'copyright']

