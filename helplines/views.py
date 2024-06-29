from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from .models import *


def get_helpline_data(request):
    id = request.GET.get('id')
    print("id------")
    print(id)
    print(id)
    data = AddHelpline.objects.get(id=id)
    print(data)
    context = dict()
    context['data'] = data
    html_form = render_to_string('web/helplines_data.html', context)
    return JsonResponse({'html_form': html_form})
