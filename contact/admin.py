from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

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

