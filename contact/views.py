from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from sweetify import sweetify

from contact.models import Contact


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