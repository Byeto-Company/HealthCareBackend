from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget
from .models import *

# Inline classes for related models
class WorkTitleInline(admin.TabularInline):
    model = WorkTitle
    extra = 1  # Number of empty forms to display


class ManagerTitleInline(admin.TabularInline):
    model = ManagerTitle
    extra = 1  # Number of empty forms to display


class CertificateTitleInline(admin.TabularInline):
    model = CertificateTitle
    extra = 1  # Number of empty forms to display


class HeroButtonInline(admin.TabularInline):
    model = HeroButton
    extra = 1  # Number of empty forms to display


class HeroImageInline(admin.TabularInline):
    model = HeroImage
    extra = 1  # Number of empty forms to display


class HeroLogoInline(admin.TabularInline):
    model = HeroLogo
    extra = 1  # Number of empty forms to display


class HeroBodyLogoInline(admin.TabularInline):
    model = HeroBodyLogo
    extra = 1  # Number of empty forms to display


class DemoFormInline(admin.TabularInline):
    model = DemoForm
    extra = 1


class AboutProjectInline(admin.TabularInline):
    model = AboutProject
    extra = 1


class FooterSocialInline(admin.TabularInline):
    model = FooterSocial
    extra = 1


class FooterEmailInline(admin.TabularInline):
    model = FooterEmail
    extra = 1


class FooterPhoneInline(admin.TabularInline):
    model = FooterPhone
    extra = 1


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
    inlines = [WorkTitleInline]

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
    inlines = [ManagerTitleInline]


@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    inlines = [CertificateTitleInline]


@admin.register(Hero)
class HeroAdmin(ModelAdmin):
    inlines = [HeroButtonInline, HeroImageInline, HeroLogoInline, HeroBodyLogoInline]


@admin.register(Demo)
class DemoAdmin(ModelAdmin):
    inlines = [DemoFormInline]



@admin.register(AboutUs)
class AboutUsAdmin(ModelAdmin):
    inlines = [AboutProjectInline]


@admin.register(Footer)
class FooterAdmin(ModelAdmin):
    inlines = [FooterSocialInline, FooterEmailInline, FooterPhoneInline]


@admin.register(CertificateTitle)
class CertificateTitleAdmin(ModelAdmin):
    pass


@admin.register(WorkTitle)
class WorkTitleAdmin(ModelAdmin):
    pass


@admin.register(ManagerTitle)
class ManagerTitleAdmin(ModelAdmin):
    pass


@admin.register(HeaderLink)
class HeaderLinkAdmin(ModelAdmin):
    pass

@admin.register(MetaTagsPage)
class MetaTagsPage(ModelAdmin):
    pass