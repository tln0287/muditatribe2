# Generated by Django 5.0.6 on 2024-06-28 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='activity_date',
            new_name='article_date',
        ),
    ]