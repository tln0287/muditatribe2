from django.contrib import admin
from .models import User,UserGroups
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(User)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['id','u_id','first_name']

    search_fields = ('username','u_id','email','first_name')

@admin.register(UserGroups)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['id','user','group','is_active','is_default','is_block']
    list_filter = ['group']
    search_fields = ('user__username',)
admin.site.unregister(Group)

@admin.register(Group)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['id','name']




