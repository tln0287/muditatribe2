from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from usermanagement.models import User


def get_counsellor_data(request):
    id = request.GET.get('id')
    data = User.objects.get(id=id)

    context = dict()
    context['data'] = data
    html_form = render_to_string('web/counsellor_data.html', context, request=request)

    return JsonResponse({'html_form': html_form})