# Generated by Django 2.1 on 2018-08-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20180815_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='star',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], max_length=1, verbose_name='평점'),
        ),
    ]
