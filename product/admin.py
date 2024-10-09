from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, Product, Feature, Capability, Slide


class ProductInline(TabularInline):
    model = Product
    extra = 1

class FeatureInline(TabularInline):
    model = Feature
    extra = 1

class SlideInline(TabularInline):
    model = Slide
    extra = 1

class CapabilityInline(TabularInline):
    model = Capability
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
    inlines = [SlideInline, FeatureInline, CapabilityInline]
