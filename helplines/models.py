from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class AddHelpline(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to="helplines/", null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    phone = models.CharField(max_length=1000,null=True,blank=True)
    language = models.CharField(max_length=500,null=True,blank=True)
    timings = models.CharField(max_length=1000,null=True,blank=True)
    location = models.CharField(max_length=1000,null=True,blank=True)
    email = models.CharField(max_length=500,null=True,blank=True)
    website = models.CharField(max_length=500,null=True,blank=True)


    def admin_photo(self):
        if self.photo:
            return mark_safe('<img src="{}" width="100" />'.format(self.photo.url))
        else:
            return '(No photo)'

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
