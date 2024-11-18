from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(Blog)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['admin_photo','publish','blog_date']
    search_fields = ('title',)

@admin.register(BlogComments)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['blog','name','email','phone']
    search_fields = ('name','phone')

# Register your models here.
@admin.register(Contact)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'phone','created_at']
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone')

# Register your models here.
@admin.register(MentalHealthProfessional)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'phone','created_at']
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone')

# Register your models here.
@admin.register(MentalHealthVolunteer)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'phone','created_at']
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone')


# Register your models here.
@admin.register(ExpertCategory)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ('name',)

# Register your models here.
@admin.register(AddCounsellor)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['user','created_at']
    raw_id_fields = ('user',)
    search_fields = ('user__first_name',)
    filter_horizontal = ('expertise_in',)  # Ensure this is a ManyToManyField


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

@admin.register(AddHelpline)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['admin_photo','name','description']
    search_fields = ('name','description','phone')


# Register your models here.
@admin.register(Exceptions)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['error_name','created_at']
    list_filter = ['created_at']
    search_fields = ('error_name',)
