from django.shortcuts import render

# Create your views here.
from blog.models import Blog
from counsellor.encryption_util import decrypt


def blog_details(request,id):
    id = decrypt(id)
    data = Blog.objects.get(id=id)
    context = dict()
    context['data'] = data
    return render(request,'web/blog_details.html',context)
