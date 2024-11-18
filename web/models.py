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
    article_type = models.CharField(max_length=500, blank=True, null=True)
    article_date = models.DateField(null=True,blank=True)

    def admin_photo(self):
        if self.article_main_image:
            return mark_safe('<img src="{}" width="100" />'.format(self.article_main_image.url))
        else:
            return '(No photo)'



    class Meta:
        verbose_name_plural = "Add Article"


from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=1500, null=True, blank=True)
    email = models.CharField(max_length=1500, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)




class MentalHealthProfessional(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True,blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    profession = models.CharField(max_length=100,null=True,blank=True)
    cv = models.FileField(upload_to='cvs/',null=True,blank=True)
    specialisation = models.CharField(max_length=255,null=True,blank=True)
    degree = models.FileField(upload_to='degrees/',null=True,blank=True)
    experience = models.CharField(max_length=255,null=True,blank=True)
    photo = models.ImageField(upload_to='photos/',null=True,blank=True)
    delivery_mode = models.CharField(max_length=50, null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models

class MentalHealthVolunteer(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    specialisation = models.CharField(max_length=255, null=True, blank=True)
    degree = models.FileField(upload_to='degrees/', null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    delivery_mode = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AlternateTherapist(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    specialisation = models.CharField(max_length=255, null=True, blank=True)
    degree = models.FileField(upload_to='degrees/', null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    delivery_mode = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from user_management.models import User

class ExpertCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Expert Categories"



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

class UserTestimonial(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=1500, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class AddCounsellor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="counsellors", null=True, blank=True)
    photo = models.ImageField(upload_to='counsellor/',null=True,blank=True)
    expertise_in = models.ManyToManyField(ExpertCategory, related_name="expert_in", blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Counsellor {self.id} - {self.user.username if self.user else 'No User'}"


# Create your models here.
class DonatedUser(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    razorpay_order_id = models.CharField(max_length=100,blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    txn_id = models.CharField(max_length=1500, null=True, blank=True)
    payment_type = models.CharField(max_length=1500, null=True, blank=True)
    name = models.CharField(max_length=1500, null=True, blank=True)
    email = models.CharField(max_length=1500, null=True, blank=True)
    address = models.TextField(null=True,blank=True)
    amount = models.CharField(max_length=500, null=True, blank=True)
    paid_amount = models.CharField(max_length=500, null=True, blank=True)
    paid_date = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    paid = models.BooleanField(default=False)
    indian_citizen = models.BooleanField(default=False,null=True)
    pan_card = models.FileField(upload_to='pancards',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Created')


class Payment(models.Model):
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Created')
    created_at = models.DateTimeField(auto_now_add=True)

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


class Exceptions(models.Model):
    error_name = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
# Create your models here.

from django.utils.translation import gettext_lazy as _
# Create your models here.


class Blog(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)
    blog_main_image = models.ImageField(upload_to='Article/',blank=True, null=True)
    publish = models.BooleanField(default=False)
    blog_date = models.DateField(null=True,blank=True)
    created_by = models.CharField(max_length=500,null=True,blank=True)
    user_id = models.CharField(max_length=200,null=True,blank=True)
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.blog_main_image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    class Meta:
        verbose_name_plural = "Add Blog"

class BlogComments(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    blog = models.ForeignKey(Blog,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    comment = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name_plural = "Blog Comments"


