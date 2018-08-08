from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=100, verbose_name='작성자')
    message = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#class Grade(models.Model):
 # Product = models.OneToOneField(Product, on_delete=models.cascade)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    spend = models.CharField(max_length=20, verbose_name='구매내역')