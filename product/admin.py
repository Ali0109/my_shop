from django.contrib import admin

from product.models import *


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'media',
    ]
    search_fields = ['title', 'description']
    # list = ['id', 'title', 'description']
