from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from sweetify import sweetify
import urllib
import json
from django.conf import settings
from contact.models import Contact
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *

def submit_form(request):
    try:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success']:
            if request.method == 'POST':
                name = request.POST['name']
                phone = request.POST['phone']
                gender = request.POST.get('gender', '')
                email = request.POST['email']
                dob = request.POST['dob']
                city = request.POST['city']
                profession = request.POST['profession']
                specialisation = request.POST['specialisation']
                experience = request.POST['experience']
                delivery_mode = request.POST['delivery_mode']
                description = request.POST['description']
                message = request.POST['message']

                cv = request.FILES['cv']
                degree = request.FILES['degree']
                photo = request.FILES['photo']

                new_professional = MentalHealthProfessional(
                    name=name,
                    phone=phone,
                    gender=gender,
                    email=email,
                    dob=dob,
                    city=city,
                    profession=profession,
                    specialisation=specialisation,
                    experience=experience,
                    delivery_mode=delivery_mode,
                    description=description,
                    message=message,
                    cv=cv,
                    degree=degree,
                    photo=photo
                )
                new_professional.save()
                sweetify.success(request,'successfully submitted')
        else:
            messages.error(request, 'Please Enter Captcha!')
            return redirect(request.META.get('HTTP_REFERER'))
        return redirect('professional')  # Replace 'success_page' with your success URL name
    except:
        return render(request, 'professional')  # Replace 'form_page.html' with your form template name

def submit_form2(request):
    try:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success']:
            if request.method == 'POST':
                name = request.POST['name']
                phone = request.POST['phone']
                gender = request.POST.get('gender', '')
                email = request.POST['email']
                dob = request.POST['dob']
                city = request.POST['city']
                specialisation = request.POST['specialisation']
                experience = request.POST['experience']
                delivery_mode = request.POST['delivery_mode']
                description = request.POST['description']
                message = request.POST['message']

                cv = request.FILES['cv']
                degree = request.FILES['degree']
                photo = request.FILES['photo']

                new_professional = MentalHealthVolunteer(
                    name=name,
                    phone=phone,
                    gender=gender,
                    email=email,
                    dob=dob,
                    city=city,

                    specialisation=specialisation,
                    experience=experience,
                    delivery_mode=delivery_mode,
                    description=description,
                    message=message,
                    cv=cv,
                    degree=degree,
                    photo=photo
                )
                new_professional.save()
                messages.success(request,'successfully submitted')
                return redirect('volunteer')  # Replace 'success_page' with your success URL name
        else:
            messages.error(request, 'Please Enter Captcha!')
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'volunteer')  # Replace 'form_page.html' with your form template name
    except:
        return render(request, 'volunteer')  # Replace 'form_page.html' with your form template name


def submit_form3(request):
    try:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success']:
            if request.method == 'POST':
                name = request.POST['name']
                phone = request.POST['phone']
                gender = request.POST.get('gender', '')
                email = request.POST['email']
                dob = request.POST['dob']
                city = request.POST['city']
                specialisation = request.POST['specialisation']
                experience = request.POST['experience']
                delivery_mode = request.POST['delivery_mode']
                description = request.POST['description']
                message = request.POST['message']

                cv = request.FILES['cv']
                degree = request.FILES['degree']
                photo = request.FILES['photo']

                new_professional = AlternateTherapist(
                    name=name,
                    phone=phone,
                    gender=gender,
                    email=email,
                    dob=dob,
                    city=city,

                    specialisation=specialisation,
                    experience=experience,
                    delivery_mode=delivery_mode,
                    description=description,
                    message=message,
                    cv=cv,
                    degree=degree,
                    photo=photo
                )
                new_professional.save()
                messages.success(request,'successfully submitted')
                return redirect('alternate_therapist')  # Replace 'success_page' with your success URL name
        else:
            messages.error(request, 'Please Enter Captcha!')
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'alternate_therapist')  # Replace 'form_page.html' with your form template name
    except:
        return render(request, 'alternate_therapist')  # Replace 'form_page.html' with your form template name




def add_contact(request):
    try:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success']:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']

            obj = Contact(name=name, email=email,phone=phone,description=message)
            obj.save()
            messages.success(request,'Thank you! we will contact you soon.')

            return redirect('/')
        else:
            messages.error(request, 'Please Enter Captcha!')
            return redirect(request.META.get('HTTP_REFERER'))
    except:
        return redirect('/')