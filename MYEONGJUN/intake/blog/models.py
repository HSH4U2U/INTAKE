from django.db import models

# Create your models here.
class Comment(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.cascade)
    author = models.CharField(max_length=100, verbose_name='작성자')
    message = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Grade(models.Model):
 Product = models.OneToOneField(Product, on_delete=models.cascade)

class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
