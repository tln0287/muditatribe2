import json
import urllib
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
# Create your views here.
def add_testimonial(request):
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
            message = request.POST['message']
            email = request.POST['email']
            obj =UserTestimonial(name=name,description=message,email=email,publish=False)
            obj.save()
            messages.success(request, "Submitted successfully")

            return redirect('/')
        messages.error(request, "Please enter captch")
        return redirect('/')
    except:
        messages.error(request, "Unable to add")
        return redirect('/')
