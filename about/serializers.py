from rest_framework import serializers
from .models import *

class WorkTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTags
        exclude = ('id',)
        read_only_fields = [id, ]


class WorkFieldSerializer(serializers.ModelSerializer):
    tags = WorkTagSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()
    class Meta:
        model = WorkField
        exclude = ('id',)
        
        read_only_fields = [id, ]
    def get_image(self, obj):
        data = {
            'image': obj.image.url if obj.image else None,
            'alt': obj.title
        }
        return data

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
        fields = ['title', 'description']

class AboutUsSerializer(serializers.ModelSerializer):
    projects = AboutProjectSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = ['image', 'title', 'description', 'projects']

class FooterSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSocial
        fields = ['soical', 'link']

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
    emails = serializers.SerializerMethodField()
    phones = serializers.SerializerMethodField()

    class Meta:
        model = Footer
        fields = ['title', 'description', 'address', 'socials', 'emails', 'phones', 'copyright']
    def get_emails(self, obj):
        emails = FooterEmail.objects.all()
        list_emails = [footeremail.email for footeremail in emails]
        return list_emails
    def get_phones(self, obj):
        phones = FooterPhone.objects.all()
        list_phones = [footerphone.phone for footerphone in phones]
        return list_phones

class WorkTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTitle
        fields = ['title', 'description']

class ManagerTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerTitle
        fields = ['title', 'description']

class CertificateTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateTitle
        fields = ['title', 'description']
