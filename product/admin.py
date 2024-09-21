from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, Product, Feature, Detail

class ProductInline(TabularInline):
    model = Product
    extra = 1

class FeatureInline(TabularInline):  # Or StackedInline
    model = Feature
    extra = 1

class DetailInline(TabularInline):  # Or StackedInline
    model = Detail
    extra = 1

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    inlines = [FeatureInline, DetailInline]
