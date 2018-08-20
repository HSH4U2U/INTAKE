from django.contrib import admin
from .models import Product, Comment, Category


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'product_image', 'product_price_before', 'product_price', 'product_register', 'product_detail', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'star', 'content', 'created_at', 'updated_at', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
