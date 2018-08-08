from django.contrib import admin
from blog.models import Comment, Profile

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):pass
