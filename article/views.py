from django.shortcuts import render

# Create your views here.
from .models import Articles
from counsellor.encryption_util import decrypt


def article_details(request,id):
    id = decrypt(id)
    data = Articles.objects.get(id=id)
    context = dict()
    context['data'] = data
    return render(request,'web/article_details.html',context)
