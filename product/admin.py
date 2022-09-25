from django.contrib import admin

from product.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'created_at',
    ]
    search_fields = ['title', 'description']
    list_filter = ['created_at']


@admin.register(ProductMedia)
class ProductMediaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product',
        'file',
        'extension',
        'file_name',
        'file_path',
        'created_at',
    ]
    search_fields = ['product__title', 'product__id']
    list_filter = ['extension', 'created_at']
    # list = ['id', 'title', 'description']
