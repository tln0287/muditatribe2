from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

# Create your models here.

from django.utils.safestring import mark_safe

class User(AbstractUser):
    phone = models.CharField(max_length=100,null=True,blank=True)
    first_name = models.CharField(max_length=150,null=True,blank=True)
    last_name = models.CharField(max_length=150,null=True,blank=True)
    email = models.CharField(max_length=150,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    qualification = models.CharField(max_length=500,null=True,blank=True)
    location = models.CharField(max_length=500,null=True,blank=True)
    language = models.CharField(max_length=500,null=True,blank=True)
    gender = models.CharField(max_length=30,null=True,blank=True)
    designation = models.CharField(max_length=100,null=True,blank=True)
    experience = models.CharField(max_length=100,null=True,blank=True)
    expertise = models.TextField(null=True,blank=True)
    u_id = models.CharField(max_length=15,null=True,blank=True)
    photo = models.ImageField(upload_to="profile_photo/",null=True,blank=True)
    modal_image = models.ImageField(upload_to="profile_photo/",null=True,blank=True)
    flag_counter = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user",
        related_query_name="user",
        through="UserGroups"
    )

    def admin_photo(self):
        if self.photo:
            return mark_safe('<img src="{}" width="100" />'.format(self.photo.url))
        else:
            return '(No photo)'

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True


    class Meta:
        db_table = "auth_user"




class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userOf")
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name="groupOf")
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)

    class Meta:
        db_table = "user_groups"
        verbose_name_plural = "User Groups"



class UserSupport(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="USERSUPPORT")
    title = models.CharField(max_length=1000, blank=True, null=True)
    query_created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    query_status = models.IntegerField(default=0,null=True,blank=True)
    reply_status = models.IntegerField(default=0,null=True,blank=True)


class UserSupportComment(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="USERSUPPORTComments")
    support = models.ForeignKey(UserSupport, on_delete=models.CASCADE, related_name="USERComments")
    comments = models.TextField(null=True,blank=True)
    file = models.FileField(upload_to="support",null=True,blank=True)
    comment_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)