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
