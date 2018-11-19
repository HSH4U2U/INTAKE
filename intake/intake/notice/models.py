from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100, verbose_name='제목')
    content= models.TextField()

    updated_at=models.DateTimeField(auto_now=True, verbose_name='날짜')

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.title
