from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=20, verbose_name='상품명',)
    product_price_before = models.CharField(max_length=100, verbose_name='정가',)
    product_price = models.CharField(max_length=100, verbose_name='가격',)
    product_register = models.DateTimeField(auto_now_add=True, verbose_name='상품 등록일')
    product_detail = models.TextField(verbose_name='상품 설명')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.product_name


class Comment(models.Model):
    STATUS_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, verbose_name='작성자')   # Profile의 user와 같은 거?? 따로 부름??
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, verbose_name='해당 상품') #blank true 지우기 위 여기 둘 다
    star = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, verbose_name='평점')
    content = models.TextField(verbose_name='댓글 내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('main_app:product')


    # def __str__(self):
    #     return self.author

