# Generated by Django 5.0.6 on 2024-06-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0004_donateduser_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='donateduser',
            name='email',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]