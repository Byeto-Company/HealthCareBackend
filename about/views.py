from django.db.models import Count

from customer.serializer import CustomerSerializer, CustomerProvinceSerializer
from product.models import Product
from product.serializers import ProductSerializer
from .serializers import *
from .models import WorkField, WorkTags, Manager, Certificate
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView 
from .models import *
from rest_framework.views import Response
from rest_framework import status
from customer.models import Customer, Province


class GetFooterView(APIView):
    def get(self, request):
        footer = Footer.objects.first()  # Assuming one footer
        footer_serializer = FooterSerializer(footer)
        return Response(footer_serializer.data, status=status.HTTP_200_OK)


# class GetDataBaseView(APIView):
#     def get(self, request):
#         workfields = WorkField.objects.all()
#         workfield_serilizer = WorkFieldSerializer(instance=workfields, many=True)
#         managers = Manager.objects.all()
#         managers_seriliazer = ManagerSerializer(instance=managers, many=True)
#         certificates = Certificate.objects.all()
#         certificates_seriliazer = CertificateSerializer(instance=certificates, many=True)
#
#         about_data = {
#             "workfields": workfield_serilizer.data,
#             "products" : 'developing',
#             "managers": managers_seriliazer.data,
#             "certificates" : certificates_seriliazer.data,
#             "markaz_darmani_count": Customer.objects.all().count(),
#             "category_project_count": {
#                 "some_bullshit_category": "some_bullshit_number its developing "
#             },
#
#         }
#         return Response(about_data, status=status.HTTP_200_OK)



class WebsiteContentView(APIView):
    def get(self, request):
        # Hero Section
        hero = Hero.objects.first()  # Assuming there is only one hero section
        hero_serializer = HeroSerializer(hero)

        # Work Fields Section
        work_fields = WorkField.objects.all()
        work_fields_serializer = WorkFieldSerializer(work_fields, many=True)

        # Products Section
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)

        # Managers Section
        managers = Manager.objects.all()
        managers_serializer = ManagerSerializer(managers, many=True)

        # Certificates Section
        certificates = Certificate.objects.all()
        certificates_serializer = CertificateSerializer(certificates, many=True)

        # Customers Section
        province_customer_counts = Province.objects.annotate(
            customer_count=Count('customer')
        )
        customer_serializer = CustomerProvinceSerializer(province_customer_counts, many=True)

        # About Us Section
        about_us = AboutUs.objects.first()  # Assuming one about_us
        about_serializer = AboutUsSerializer(about_us)

        footer = Footer.objects.first()  # Assuming one footer
        footer_serializer = FooterSerializer(footer)

        demo = Demo.objects.first()
        demo_serializer = DemoSerializer(demo)

        logo = HeroLogo.objects.first()
        logo_serializer = HeroLogoSerializer(logo)

        body_logo = HeroBodyLogo.objects.first()
        body_logo_serializer = HeroBodyLogoSerializer(body_logo)

        work_title = WorkTitle.objects.first()
        work_title_serializer = WorkTitleSerializer(work_title)

        manager_title = ManagerTitle.objects.first()
        manager_title_serializer = ManagerTitleSerializer(manager_title)

        certificate_title = CertificateTitle.objects.first()
        certificate_title_serializer = CertificateTitleSerializer(certificate_title)

        return Response({
            "logo": logo_serializer.data,
            "body_logo": body_logo_serializer.data,
            "hero": hero_serializer.data,
            "work_fields": {
                "title": work_title.title,
                "description": work_title.description,
                "fields": work_fields_serializer.data,
            },
            "products": products_serializer.data,

            "leaders":{
                'title': manager_title.title,
                'description': manager_title.description,
                'members': managers_serializer.data
            },
            "certificates":{
                'title': certificate_title.title,
                'description': certificate_title.description,
                'items':certificates_serializer.data
                },
            "states": customer_serializer.data,
            "about_us": about_serializer.data,
            "demo": demo_serializer.data,
            "footer": footer_serializer.data,
        }, status=status.HTTP_200_OK)