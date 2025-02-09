# Generated by Django 5.0.7 on 2024-07-17 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site_backend', '0002_tag_name_en_tag_name_ru_tag_name_uz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryable_type', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('name_uz', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('resized_images', models.JSONField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog_site_backend.categories')),
            ],
        ),
    ]
