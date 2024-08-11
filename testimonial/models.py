from django.db import models

# Create your models here.
class UserTestimonial(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=1500, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)