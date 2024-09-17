from .serializers import *
from .models import WorkField, WorkTags, Manager, Certificate
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView 
from .models import *
from rest_framework.views import Response
from rest_framework import status
from customer.models import Customer


class GetFooterView(APIView):
    def get(self, request):
        socials = Soical.objects.all()
        social_ser = SocialSerializer(instance=socials, many=True)
        emails = EmailModel.objects.all()
        emails_ser = EmailSerializer(instance=emails, many=True)
        numbers = NumberModel.objects.all()
        number_ser = NumberSerializer(instance=numbers, many=True)
        footer_data = {
            "socials": social_ser.data,
            'emails': emails_ser.data,
            "numbers": number_ser.data,
        }
        return Response(footer_data, status=status.HTTP_200_OK)


class GetDataBaseView(APIView):
    def get(self, request):
        workfields = WorkField.objects.all()
        workfield_serilizer = WorkFieldSerializer(instance=workfields, many=True)
        managers = Manager.objects.all()
        managers_seriliazer = ManagerSerializer(instance=managers, many=True)
        certificates = Certificate.objects.all()
        certificates_seriliazer = CertificateSerializer(instance=certificates, many=True)

        about_data = {
            "workfields": workfield_serilizer.data,
            "products" : 'developing',
            "managers": managers_seriliazer.data,
            "certificates" : certificates_seriliazer.data,
            "markaz_darmani_count": Customer.objects.all().count(),
            "category_project_count": {
                "some_bullshit": "some_bullshit"
            },
            
        }
        return Response(about_data, status=status.HTTP_200_OK)