# Generated by Django 5.1 on 2024-10-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdemo',
            name='module',
            field=models.CharField(default='', max_length=100, verbose_name='نام ماژول'),
            preserve_default=False,
        ),
    ]
