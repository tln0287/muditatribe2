from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
# Create your models here.

from django.utils.translation import gettext_lazy as _

# Create your models here.
class Articles(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)
    article_main_image = models.ImageField(upload_to='Article/',blank=True, null=True)
    publish = models.BooleanField(default=False)
    article_date = models.DateField(null=True,blank=True)
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.article_main_image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True



    class Meta:
        verbose_name_plural = "Add Article"
