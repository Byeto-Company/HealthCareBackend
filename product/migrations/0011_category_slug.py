# Generated by Django 5.1 on 2024-10-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_product_icon_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=100, null=True, unique=True, verbose_name='نام یکتا'),
        ),
    ]
