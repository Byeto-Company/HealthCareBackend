# Generated by Django 5.1 on 2024-10-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(default='', verbose_name='متا تگ دسکریپشن'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keyword',
            field=models.TextField(default='', help_text='لطفا با کاما وارد کنید', verbose_name='متا تگ کیورد'),
            preserve_default=False,
        ),
    ]
