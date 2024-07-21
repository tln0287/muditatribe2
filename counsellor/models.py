from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from usermanagement.models import User

class ExpertCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Expert Categories"

class AddCounsellor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="counsellors", null=True, blank=True)
    photo = models.ImageField(upload_to='counsellor/',null=True,blank=True)
    expertise_in = models.ManyToManyField(ExpertCategory, related_name="expert_in", blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Counsellor {self.id} - {self.user.username if self.user else 'No User'}"