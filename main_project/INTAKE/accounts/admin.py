from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'address', 'email', ]
