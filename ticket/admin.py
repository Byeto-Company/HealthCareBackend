from django.contrib import admin
from .models import RequestDemo, ContactUs
import jdatetime


def gregorian_to_jalali(gregorian_date):
    if gregorian_date:
        jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
        return jalali_date.strftime('%Y/%m/%d')
    return None


class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'company_name', 'jalali_requested_at')
    readonly_fields = ('jalali_requested_at',)

    def jalali_requested_at(self, obj):
        return gregorian_to_jalali(obj.requested_at)

    jalali_requested_at.short_description = "تاریخ درخواست (شمسی)"


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'jalali_contacted_at')
    readonly_fields = ('jalali_contacted_at',)

    def jalali_contacted_at(self, obj):
        return gregorian_to_jalali(obj.contacted_at)

    jalali_contacted_at.short_description = "تاریخ تماس (شمسی)"


# Registering the models with the customized admin classes
admin.site.register(RequestDemo, RequestDemoAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
