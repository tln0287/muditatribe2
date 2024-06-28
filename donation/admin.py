from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(Payment)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['razorpay_order_id', 'razorpay_payment_id', 'razorpay_signature','amount','status']
    list_filter = ('status', 'created_at', 'amount')


# Register your models here.
@admin.register(DonatedUser)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name','amount','paid','paid_amount','paid_date','phone','pan_card','razorpay_order_id','txn_id','payment_type']
    list_filter = ('paid','created_at','paid_date')
    search_fields = ('name','phone')
