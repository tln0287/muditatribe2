# Generated by Django 5.0.6 on 2024-06-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donateduser',
            name='order_id',
        ),
        migrations.AddField(
            model_name='donateduser',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='donateduser',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='donateduser',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
