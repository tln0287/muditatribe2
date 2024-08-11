from django.db import models

# Create your models here.
class DonatedUser(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    razorpay_order_id = models.CharField(max_length=100,blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    txn_id = models.CharField(max_length=1500, null=True, blank=True)
    payment_type = models.CharField(max_length=1500, null=True, blank=True)
    name = models.CharField(max_length=1500, null=True, blank=True)
    email = models.CharField(max_length=1500, null=True, blank=True)
    address = models.TextField(null=True,blank=True)
    amount = models.CharField(max_length=500, null=True, blank=True)
    paid_amount = models.CharField(max_length=500, null=True, blank=True)
    paid_date = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    paid = models.BooleanField(default=False)
    indian_citizen = models.BooleanField(default=False,null=True)
    pan_card = models.FileField(upload_to='pancards',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Created')


class Payment(models.Model):
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Created')
    created_at = models.DateTimeField(auto_now_add=True)