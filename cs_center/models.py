from django import forms
from django.db import models
from django.urls import reverse


def min_length_2_validator(value):
    if len(value) < 2 or len(value) > 10:
        raise forms.ValidationError('2글자 이상 10글자 이하로 입력해주세요.')



class Post(models.Model):
    name = models.CharField(max_length=100, verbose_name='이름', validators=[min_length_2_validator])
    email = models.CharField(max_length=100, verbose_name='이메일 주소')
    phone_number = models.CharField(max_length=100, verbose_name='휴대전화 번호(선택)', blank='true')
    title = models.TextField(verbose_name='문의 제목')
    content = models.TextField(verbose_name='문의 내용')
    profile = models.CharField(max_length=100, verbose_name='인테이크 개인정보취급방침')


    def get_absolute_url(self):
      return reverse('ask:post_detail', args=[self.id])



