from django.db import models

# Create your models here.

class Exceptions(models.Model):
    error_name = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
