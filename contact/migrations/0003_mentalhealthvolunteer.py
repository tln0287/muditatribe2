# Generated by Django 5.0.6 on 2024-06-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_mentalhealthprofessional'),
    ]

    operations = [
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
    ]
