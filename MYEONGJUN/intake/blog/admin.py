from django.contrib import admin
from intake.models import Comment, Grade

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):pass
