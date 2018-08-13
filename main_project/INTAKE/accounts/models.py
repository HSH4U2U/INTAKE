from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='사용자')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    # spend = models.CharField(max_length=20, verbose_name='구매내역')            #결제 기능 추가 후 변경 예정