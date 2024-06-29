from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from sweetify import sweetify

from contact.models import Contact
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *

def submit_form(request):
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
        return redirect('professional')  # Replace 'success_page' with your success URL name

    return render(request, 'professional')  # Replace 'form_page.html' with your form template name

def submit_form2(request):
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
        sweetify.success(request,'successfully submitted')
        return redirect('volunteer')  # Replace 'success_page' with your success URL name

    return render(request, 'volunteer')  # Replace 'form_page.html' with your form template name


def add_contact(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        obj = Contact(name=name, email=email,phone=phone,description=message)
        obj.save()
        sweetify.success(request,'Thankyou we will contact you soon.')

        return redirect('/')
    except:
        return redirect('/')