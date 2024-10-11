from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget
from .models import *

@admin.register(WorkTags)
class WorkTagsAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(WorkField)
class WorkFieldAdmin(ModelAdmin):
    list_display = ('title', 'ordering',)
    search_fields = ('title',)
    ordering = ('ordering',)

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

@admin.register(Manager)
class ManagerAdmin(ModelAdmin):
    list_display = ('name', 'ordering',)
    search_fields = ('name',)
    ordering = ('ordering',)

@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Soical)
class SoicalAdmin(ModelAdmin):
    list_display = ('soical', 'link',)
    search_fields = ('soical',)
    ordering = ('soical',)

@admin.register(NumberModel)
class NumberModelAdmin(ModelAdmin):
    list_display = ('number', 'ordering',)
    ordering = ('ordering',)

@admin.register(EmailModel)
class EmailModelAdmin(ModelAdmin):
    list_display = ('email', 'ordering',)
    ordering = ('ordering',)


@admin.register(Hero)
class HeroAdmin(ModelAdmin):
    pass


@admin.register(HeroButton)
class HeroButtonAdmin(ModelAdmin):
    pass


@admin.register(HeroImage)
class HeroImageAdmin(ModelAdmin):
    pass


@admin.register(HeroLogo)
class HeroLogoAdmin(ModelAdmin):
    pass

@admin.register(HeroBodyLogo)
class HeroBodyLogoAdmin(ModelAdmin):
    pass

@admin.register(Demo)
class DemoAdmin(ModelAdmin):
    pass


@admin.register(DemoForm)
class DemoFormAdmin(ModelAdmin):
    pass


@admin.register(AboutUs)
class AboutUsAdmin(ModelAdmin):
    pass


@admin.register(AboutProject)
class AboutProjectAdmin(ModelAdmin):
    pass


@admin.register(Footer)
class FooterAdmin(ModelAdmin):
    pass


@admin.register(FooterSocial)
class FooterSocialAdmin(ModelAdmin):
    pass


@admin.register(FooterEmail)
class FooterEmailAdmin(ModelAdmin):
    pass


@admin.register(FooterPhone)
class FooterPhoneAdmin(ModelAdmin):
    pass


@admin.register(CertificateTitle)
class CertificateTitleAdmin(ModelAdmin):
    pass


@admin.register(WorkTitle)
class WorkTitleAdmin(ModelAdmin):
    pass
@admin.register(ManagerTitle)
class ManagerTitleAdmin(ModelAdmin):
    pass


