from django.contrib import admin
from .models import (
    WorkTags,
    WorkField,
    WorkTitle,
    Manager,
    ManagerTitle,
    Certificate,
    CertificateTitle,
    Soical,
    NumberModel,
    EmailModel,
    Hero,
    HeroButton,
    HeroImage,
    HeroLogo,
    HeroBodyLogo,
    Demo,
    DemoForm,
    AboutUs,
    AboutProject,
    Footer,
    FooterSocial,
    FooterEmail,
    FooterPhone,
)

class WorkTitleInline(admin.TabularInline):
    model = WorkTitle
    extra = 1  # Number of empty forms to display

class WorkFieldAdmin(admin.ModelAdmin):
    inlines = [WorkTitleInline]

class ManagerTitleInline(admin.TabularInline):
    model = ManagerTitle
    extra = 1

class ManagerAdmin(admin.ModelAdmin):
    inlines = [ManagerTitleInline]

class CertificateTitleInline(admin.TabularInline):
    model = CertificateTitle
    extra = 1

class CertificateAdmin(admin.ModelAdmin):
    inlines = [CertificateTitleInline]

class FooterSocialInline(admin.TabularInline):
    model = FooterSocial
    extra = 1

class FooterEmailInline(admin.TabularInline):
    model = FooterEmail
    extra = 1

class FooterPhoneInline(admin.TabularInline):
    model = FooterPhone
    extra = 1

class FooterAdmin(admin.ModelAdmin):
    inlines = [FooterSocialInline, FooterEmailInline, FooterPhoneInline]

# Register models with admin
admin.site.register(WorkTags)
admin.site.register(WorkField, WorkFieldAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Soical)
admin.site.register(NumberModel)
admin.site.register(EmailModel)
admin.site.register(Hero)
admin.site.register(HeroButton)
admin.site.register(HeroImage)
admin.site.register(HeroLogo)
admin.site.register(HeroBodyLogo)
admin.site.register(Demo)
admin.site.register(DemoForm)
admin.site.register(AboutUs)
admin.site.register(AboutProject)
admin.site.register(Footer, FooterAdmin)
