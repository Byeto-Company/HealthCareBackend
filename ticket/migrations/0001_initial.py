# Generated by Django 5.1 on 2024-09-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=150, verbose_name='موضوع')),
                ('message', models.TextField(verbose_name='پیام')),
                ('contacted_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ تماس')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس\u200cهای دریافت\u200cشده',
            },
        ),
        migrations.CreateModel(
            name='RequestDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone_number', models.CharField(max_length=15, verbose_name='شماره تلفن')),
                ('company_name', models.CharField(max_length=100, verbose_name='نام شرکت')),
                ('message', models.TextField(blank=True, null=True, verbose_name='پیام')),
                ('requested_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درخواست')),
            ],
            options={
                'verbose_name': 'درخواست دمو',
                'verbose_name_plural': 'درخواست\u200cهای دمو',
            },
        ),
    ]
