# Generated by Django 5.0.6 on 2024-06-28 16:49

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('blog_main_image', models.ImageField(blank=True, null=True, upload_to='Article/')),
                ('publish', models.BooleanField(default=False)),
                ('blog_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Add Blog',
            },
        ),
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
