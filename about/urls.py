from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path
app_name = 'about'
urlpatterns = [
    path('footer', views.GetFooterView.as_view()),
    path('main', views.WebsiteContentView.as_view()),
]