# Generated by Django 5.1 on 2024-10-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_meta_description_product_meta_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(default='', max_length=30, verbose_name='متا تایتل'),
            preserve_default=False,
        ),
    ]
