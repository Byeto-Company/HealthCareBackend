# Generated by Django 5.1 on 2024-10-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_rename_module_requestdemo_module_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndPointSendContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_link', models.URLField(verbose_name=' ارسال لینک برای پست اطلاعات')),
                ('full_name', models.BooleanField(verbose_name=' ارسال نام و نام خانوادگی')),
                ('email', models.BooleanField(verbose_name=' ارسال ایمیل')),
                ('subject', models.BooleanField(verbose_name=' ارسال موضوع')),
                ('message', models.BooleanField(verbose_name=' ارسال پیام')),
                ('contacted_at', models.BooleanField(verbose_name=' ارسال تاریخ تماس')),
            ],
            options={
                'verbose_name': 'لینک پست تیکت تماس با ما',
                'verbose_name_plural': 'لینک های پست تیکت تماس با ما',
            },
        ),
    ]
