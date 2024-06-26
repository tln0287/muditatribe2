from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Exceptions)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['error_name','created_at']
    list_filter = ['created_at']
    search_fields = ('error_name',)
