from . import views
from rest_framework.routers import DefaultRouter

app_name = 'about'
urlpatterns = [
]

router = DefaultRouter()
router.register(r'workfield', views.WorkFieldViewSet, basename='workfield')
router.register(r'worktag', views.WorkTagViewSet, basename='worktag')
router.register(r'manager', views.ManagerViewSet, basename='manager')
router.register(r'certificate', views.CertificateViewSet, basename='certificate')
urlpatterns += router.urls