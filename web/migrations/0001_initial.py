# Generated by Django 5.0.6 on 2024-11-18 05:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddHelpline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='helplines/')),
                ('description', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=1000, null=True)),
                ('language', models.CharField(blank=True, max_length=500, null=True)),
                ('timings', models.CharField(blank=True, max_length=1000, null=True)),
                ('location', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('website', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='music/')),
                ('audio', models.FileField(blank=True, null=True, upload_to='music/')),
                ('description', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=500, null=True)),
                ('music_type', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='video/')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/')),
                ('description', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=500, null=True)),
                ('youtube_vedio', models.BooleanField(default=False)),
                ('iframe', models.TextField(blank=True, null=True)),
                ('video_type', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlternateTherapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cvs/')),
                ('specialisation', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.FileField(blank=True, null=True, upload_to='degrees/')),
                ('experience', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('delivery_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('article_main_image', models.ImageField(blank=True, null=True, upload_to='Article/')),
                ('publish', models.BooleanField(default=False)),
                ('article_type', models.CharField(blank=True, max_length=500, null=True)),
                ('article_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Add Article',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('blog_main_image', models.ImageField(blank=True, null=True, upload_to='Article/')),
                ('publish', models.BooleanField(default=False)),
                ('blog_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Add Blog',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1500, null=True)),
                ('email', models.CharField(blank=True, max_length=1500, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonatedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=100, null=True)),
                ('txn_id', models.CharField(blank=True, max_length=1500, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=1500, null=True)),
                ('name', models.CharField(blank=True, max_length=1500, null=True)),
                ('email', models.CharField(blank=True, max_length=1500, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('amount', models.CharField(blank=True, max_length=500, null=True)),
                ('paid_amount', models.CharField(blank=True, max_length=500, null=True)),
                ('paid_date', models.DateTimeField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('indian_citizen', models.BooleanField(default=False, null=True)),
                ('pan_card', models.FileField(blank=True, null=True, upload_to='pancards')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Created', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Exceptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error_name', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Expert Categories',
            },
        ),
        migrations.CreateModel(
            name='MentalHealthProfessional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cvs/')),
                ('specialisation', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.FileField(blank=True, null=True, upload_to='degrees/')),
                ('experience', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('delivery_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MentalHealthVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cvs/')),
                ('specialisation', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.FileField(blank=True, null=True, upload_to='degrees/')),
                ('experience', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('delivery_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='Created', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTestimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1500, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.blog')),
            ],
            options={
                'verbose_name_plural': 'Blog Comments',
            },
        ),
        migrations.CreateModel(
            name='AddCounsellor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='counsellor/')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='counsellors', to=settings.AUTH_USER_MODEL)),
                ('expertise_in', models.ManyToManyField(blank=True, related_name='expert_in', to='web.expertcategory')),
            ],
        ),
    ]
