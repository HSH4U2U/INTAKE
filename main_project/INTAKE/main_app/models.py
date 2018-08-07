from django.db import models

# Create your models here.
class Product(models.Model):
    STATUS_CHOICES = (
        ('1', '1점'),
        ('2', '2점'),
        ('3', '3점'),
        ('4', '4점'),
        ('5', '5점'),
    )
    product_name = models.CharField(max_length=20, verbose_name='상품명',)
    product_price = models.CharField(max_length=100, verbose_name='가격',)
    product_register = models.DateTimeField(auto_now_add=True, verbose_name='상품 등록일')
    product_detail = models.TextField(verbose_name='상품 설명')
    comment = models.TextField(verbose_name='댓글')                                                       #나중에 foreign으로 정보 받아야할듯
    star = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, verbose_name='평점',)       #나중에 onetoone으로 정보 받아야할듯

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.product_name