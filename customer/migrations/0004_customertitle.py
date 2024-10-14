# Generated by Django 5.1 on 2024-10-14 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_city_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('work_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='مشتریان')),
            ],
            options={
                'verbose_name': 'عنوان صفحه مشتریان',
                'verbose_name_plural': 'عناوین صفحه مشتریان',
            },
        ),
    ]
