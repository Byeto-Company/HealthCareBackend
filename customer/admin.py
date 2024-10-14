from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Province, City, Customer, CustomerTitle
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(Province)
class ProvinceAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ('name', 'province', 'latitude', 'longitude')
    list_filter = ('province',)
    search_fields = ('name', 'province__name')
    ordering = ('province', 'name')

@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ('name', 'corporate_date', 'program_name', 'province', 'city', 'persian_corporate_date')
    list_filter = (
        ('corporate_date', JDateFieldListFilter),
        'province',
        'city',
    )
    search_fields = ('name', 'program_name', 'province__name', 'city__name')
    ordering = ('province', 'city', 'name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "city":
            province_id = request.GET.get('province') or request.POST.get('province')
            if province_id:
                kwargs["queryset"] = City.objects.filter(province_id=province_id)
            else:
                kwargs["queryset"] = City.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def persian_corporate_date(self, obj):
        return obj.persian_corporate_date()

    persian_corporate_date.short_description = 'Corporate Date (Persian)'

    class Media:
        js = ('js/admin.js',)

@admin.register(CustomerTitle)
class CustomerTitleAdmin(ModelAdmin):
    exclude = ['customer']