from django.contrib import admin
from .models import *


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

class FeatureInline(admin.TabularInline):  # Or admin.StackedInline
    model = Feature
    extra = 1

class DetailInline(admin.TabularInline):  # Or admin.StackedInline
    model = Detail
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    inlines = [FeatureInline, DetailInline]