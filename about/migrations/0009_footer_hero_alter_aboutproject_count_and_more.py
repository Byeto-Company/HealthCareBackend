# Generated by Django 5.1 on 2024-09-24 23:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_demo_demoform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('copyright', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='aboutproject',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='aboutproject',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(upload_to='about/'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='demo',
            name='image',
            field=models.ImageField(upload_to='demo/'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='subtitle',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='demo',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='demoform',
            name='demo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='form', to='about.demo'),
        ),
        migrations.AlterField(
            model_name='demoform',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='herobutton',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='herobutton',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='heroimage',
            name='alt',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='heroimage',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='herologo',
            name='alt',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='herologo',
            name='link',
            field=models.URLField(),
        ),
        migrations.CreateModel(
            name='FooterEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='about.footer')),
            ],
        ),
        migrations.CreateModel(
            name='FooterPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='about.footer')),
            ],
        ),
        migrations.CreateModel(
            name='FooterSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('alt', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='about.footer')),
            ],
        ),
        migrations.AlterField(
            model_name='herobutton',
            name='hero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buttons', to='about.hero'),
        ),
        migrations.AlterField(
            model_name='heroimage',
            name='hero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='about.hero'),
        ),
        migrations.AlterField(
            model_name='herologo',
            name='hero',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logo', to='about.hero'),
        ),
        migrations.DeleteModel(
            name='HeroSection',
        ),
    ]
