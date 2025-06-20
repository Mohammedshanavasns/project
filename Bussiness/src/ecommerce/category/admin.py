# from django.contrib import admin
# from .models import ProductCategory
#
# @admin.register(ProductCategory)
# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = ("name", "parent_category", "is_active", "created_at")
#     search_fields = ("name",)
#     list_filter = ("is_active",)

from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'is_active', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['is_active', 'created_at']