from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(UserTestimonial)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name','description','publish','created_at']
    list_filter = ('publish','created_at')
    search_fields = ('name',)
