# Generated by Django 2.1 on 2018-08-20 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20180820_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category2',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Category', verbose_name='카테고리'),
            preserve_default=False,
        ),
    ]
