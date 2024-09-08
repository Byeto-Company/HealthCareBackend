# Generated by Django 5.1 on 2024-09-08 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_main_photo_product_product_icon_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_photo',
            field=models.ImageField(upload_to='fproduct/main_photos', verbose_name='عکس اصلی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_icon_photo',
            field=models.ImageField(upload_to='fproduct/icons', verbose_name='عکس ایکون لیست محصولات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secend_photo',
            field=models.ImageField(upload_to='fproduct/secend_photos', verbose_name='عکس دوم صفحه ی محصولات'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_text', models.CharField(max_length=100, verbose_name='متن جزیات')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'جز',
                'verbose_name_plural': 'جزیات',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_text', models.TextField(verbose_name='ویژگی')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'ویژگی',
                'verbose_name_plural': 'ویژگی\u200cها',
            },
        ),
    ]
