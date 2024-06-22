from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def add_testimonial(request):
    name = request.POST['name']
    message = request.POST['message']
    obj =UserTestimonial(name=name,description=message,publish=False)
    obj.save()
    return redirect('/')
