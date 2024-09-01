from .serializers import WorkTagSerializer, WorkFieldSerializer, ManagerSerializer, CertificateSerializer, SocialSerializer
from .models import WorkField, WorkTags, Manager, Certificate
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView 
from .models import Soical
from rest_framework.views import Response
class WorkFieldViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = WorkField.objects.all()
    serializer_class = WorkFieldSerializer
    partial_update = None


class WorkTagViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = WorkTags.objects.all()
    serializer_class = WorkTagSerializer
    partial_update = None


class ManagerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    partial_update = None


class CertificateViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    partial_update = None


class SoicalView(APIView):
    serializer_class = SocialSerializer
    def get(self, request):
        socials = Soical.objects.all()
        social_ser = SocialSerializer(instance=socials, many=True)
        return Response(social_ser.data)