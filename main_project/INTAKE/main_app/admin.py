from django.contrib import admin
from .models import Product, Comment, Profile


# Register your models here.
@admin.register(Profile)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'address', 'email', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price', 'product_register', 'product_detail', ]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'star', 'message', 'created_at', 'updated_at', ]