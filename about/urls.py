from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path
app_name = 'about'
urlpatterns = [
    path('social', views.SoicalView.as_view())
]

router = DefaultRouter()
router.register(r'workfield', views.WorkFieldViewSet, basename='workfield')
router.register(r'worktag', views.WorkTagViewSet, basename='worktag')
router.register(r'manager', views.ManagerViewSet, basename='manager')
router.register(r'certificate', views.CertificateViewSet, basename='certificate')
urlpatterns += router.urls