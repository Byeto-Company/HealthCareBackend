from .serializers import WorkTagSerializer, WorkFieldSerializer, ManagerSerializer, CertificateSerializer
from .models import WorkField, WorkTags, Manager, Certificate
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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
