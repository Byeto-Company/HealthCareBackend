from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from django.conf import settings


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('about/', include('about.urls')),
    path('customer/', include('customer.urls')),
    path('accounts/', include('accounts.urls')),
    path('product/', include('product.urls')),
    path('ticket/', include('ticket.urls')),
    path('admin/', admin.site.urls),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

