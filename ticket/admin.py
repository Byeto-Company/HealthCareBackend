from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import RequestDemo, ContactUs

@admin.register(RequestDemo)
class RequestDemoAdmin(ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'company_name', 'requested_at')
    search_fields = ('full_name', 'email', 'company_name')
    ordering = ('-requested_at',)

@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'contacted_at')
    search_fields = ('full_name', 'email', 'subject')
    ordering = ('-contacted_at',)
