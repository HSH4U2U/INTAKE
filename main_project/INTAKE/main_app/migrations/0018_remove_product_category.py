# Generated by Django 2.1 on 2018-08-20 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_product_category2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
