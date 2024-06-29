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

