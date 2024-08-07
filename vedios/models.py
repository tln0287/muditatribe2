from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class AddVideo(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to="video/", null=True, blank=True)
    video = models.FileField(upload_to="video/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=500, null=True, blank=True)
    youtube_vedio = models.BooleanField(default=False)
    iframe = models.TextField(null=True, blank=True)
    video_type = models.CharField(max_length=500, null=True, blank=True)

    def admin_photo(self):
        if self.photo:
            return mark_safe('<img src="{}" width="100" />'.format(self.photo.url))
        else:
            return '(No photo)'

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
