from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20, verbose_name='카테고리명',)

    def __str__(self):
        return self.category_name

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=20, verbose_name='상품명',)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, verbose_name='카테고리')
    product_image = models.ImageField(verbose_name='상품 사진',)
    product_price_before = models.IntegerField(verbose_name='정가',)
    product_price = models.IntegerField(verbose_name='가격',)
    product_register = models.DateTimeField(auto_now_add=True, verbose_name='상품 등록일')
    product_detail = models.TextField(verbose_name='상품 설명')

    # 핳인률 계산
    def product_sale(self):
        product_sale = int(100 - 100 * int(self.product_price) / int(self.product_price_before))
        return product_sale

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.product_name


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')   # Profile의 user와 같은 거?? 따로 부름??
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='해당 상품')

    # star 선택지로
    STATUS_CHOICES2 = (
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    )
    star = models.IntegerField(choices=STATUS_CHOICES2, verbose_name='평점')
    content = models.TextField(verbose_name='댓글 내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    # comment 쓰고 다시 그 페이지로
    def get_absolute_url(self):
        return reverse('main_app:product', args=[self.product.id])


