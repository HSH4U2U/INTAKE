from django.contrib import admin
from .models import Product, Comment


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price_before', 'product_price', 'product_register', 'product_detail', ]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'star', 'content', 'created_at', 'updated_at', ]