from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(AddVideo)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['admin_photo','name','description']
    search_fields = ('name','description')
