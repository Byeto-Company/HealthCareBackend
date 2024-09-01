from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError


@admin.register(WorkTags)
class WorkTagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(WorkField)
class WorkFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'tags')
    search_fields = ('title', 'description')
    list_filter = ('tags',)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ordering')
    search_fields = ('name',)
    list_filter = ('ordering',)

    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            self.message_user(request, str(e), level='error')

    def delete_model(self, request, obj):
        raise ValidationError("Deletion of Manager instances is not allowed.")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')

@admin.register(Soical)
class SoicalAdmin(admin.ModelAdmin):
    list_display = ('soical', 'link')
