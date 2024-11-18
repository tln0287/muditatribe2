from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(User)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['admin_photo','username','email','designation']
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





@admin.register(UserSupport)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['user','title','reply_status','query_status']

@admin.register(UserSupportComment)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['user','comment_on']