# Generated by Django 5.1 on 2024-09-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_photo',
            field=models.ImageField(default='', upload_to='fproduct/<django.db.models.fields.SlugField>', verbose_name='عکس اصلی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_icon_photo',
            field=models.ImageField(default='', upload_to='fproduct/<django.db.models.fields.SlugField>', verbose_name='عکس ایکون لیست محصولات'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='secend_photo',
            field=models.ImageField(default='', upload_to='fproduct/<django.db.models.fields.SlugField>', verbose_name='عکس دوم صفحه ی محصولات'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=100, null=True, unique=True, verbose_name='نام یکتا'),
        ),
    ]
