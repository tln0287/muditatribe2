# Generated by Django 5.0.6 on 2024-06-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_remove_donateduser_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donateduser',
            name='status',
            field=models.CharField(default='Created', max_length=20),
        ),
    ]