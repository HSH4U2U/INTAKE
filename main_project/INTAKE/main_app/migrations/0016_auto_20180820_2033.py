# Generated by Django 2.1 on 2018-08-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20180819_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, verbose_name='카테고리명')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='star',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], verbose_name='평점'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(1, '밀스라이트'), (2, '피로그래밍')], verbose_name='카테고리'),
        ),
    ]
