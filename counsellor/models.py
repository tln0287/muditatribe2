from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from usermanagement.models import User

class ExpertCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class AddCounsellor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="counsellors", null=True, blank=True)
    experience = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    expertise_in = models.ManyToManyField(ExpertCategory, related_name="expert_in", blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Counsellor {self.id} - {self.user.username if self.user else 'No User'}"