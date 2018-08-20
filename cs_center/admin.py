from django.contrib import admin
from ask.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):pass