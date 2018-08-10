from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=20, verbose_name='상품명',)
    product_price = models.CharField(max_length=100, verbose_name='가격',)
    product_register = models.DateTimeField(auto_now_add=True, verbose_name='상품 등록일')
    product_detail = models.TextField(verbose_name='상품 설명')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.product_name


class Comment(models.Model):
    STATUS_CHOICES = (
        ('1', '1점'),
        ('2', '2점'),
        ('3', '3점'),
        ('4', '4점'),
        ('5', '5점'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')   # Profile의 user와 같은 거?? 따로 부름??
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='해당 상품')
    star = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, verbose_name='평점')
    message = models.TextField(verbose_name='댓글 내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    # def __str__(self):
    #     return self.author


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='사용자')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    # spend = models.CharField(max_length=20, verbose_name='구매내역')            #결제 기능 추가 후 변경 예정
