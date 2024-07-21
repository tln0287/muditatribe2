from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

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