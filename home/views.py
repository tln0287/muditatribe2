from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from article.models import Articles
from blog.models import Blog
from helplines.models import AddHelpline
from testimonial.models import UserTestimonial
from .models import *
from social_django.models import UserSocialAuth
from usermanagement.models import *
# Create your views here.
def home(request):
    testimonial = UserTestimonial.objects.filter(publish=True)
    context = dict()
    context['testi'] = testimonial
    return render(request,'web/index.html',context)

def about(request):
    return render(request,'web/about.html')

def helplines(request):
    data = AddHelpline.objects.all()
    context = dict()
    context['data'] = data
    return render(request,'web/helplines.html',context)


def activities(request):
    return render(request,'web/activities.html')

def donations(request):
    return render(request,'web/donations.html')

def counsellors(request):
    data = User.objects.filter(userOf__group__name='counsellor')
    context=dict()
    context['data'] = data
    return render(request,'web/letMeet.html',context)


def contact(request):

    return render(request,'web/joinTheTribe.html')

def breathing(request):
    return render(request,'web/breathing.html')

def guided_meditation(request):
    return render(request,'web/meditation.html')

def music(request):
    return render(request,'web/music.html')

def art(request):
    return render(request,'web/art.html')


def dance_class(request):
    return render(request,'web/dance_class.html')

def music_class(request):
    return render(request,'web/music_class.html')


def postural(request):
    return render(request,'web/postural.html')


def sound_nature(request):
    return render(request,'web/sound_nature.html')


def articles(request):
    data = Articles.objects.filter(publish=True)
    context=dict()
    context['data'] = data
    return render(request,'web/articles.html',context)

def chants(request):
    return render(request,'web/chants.html')


def login2(request):
    return render(request,'web/login.html')


def music_article(request):
    return render(request,'web/music_article.html')


def refund(request):
    return render(request,'web/cancellation.html')


def terms_conditions(request):
    return render(request,'web/terms.html')



def privacy_policy(request):
    return render(request,'web/privacy.html')


def blog(request):
    data = Blog.objects.filter(publish=True)

    context = dict()
    context['data'] = data
    return render(request,'web/blog.html',context)


def register(request):
    return render(request,'web/register.html')

def failed2(request):
    messages.error(request,'You are not authorized')
    return render(request,'web/login.html')

@login_required
def profile(request):
    return render(request,'dashboard/dashboard.html')



def volunteer(request):
    return render(request,'web/volunteer.html')


def professional(request):
    return render(request,'web/professional.html')



def add_user(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        phone=request.POST['phone']
        address = request.POST['address']
        email_check = email.split('@')
        email_address = email_check[1]
        if email_address != "gmail.com":
            messages.error(request,'Accept only for gmail')

        else:
            obj, created = User.objects.get_or_create(email=email)
            obj.first_name = name
            obj.password = "pbkdf2_sha256$390000$qjgXAopeH0sYVMjgJaESp3$ZMnGBKxZo9tj/sKf2EhCmCnS7ibAbd1KhxOStvEl0go="
            obj.last_name = name
            obj.address = address
            obj.phone = phone
            obj.email = email
            obj.save()

            obj2, created = UserGroups.objects.get_or_create(user_id=obj.id,group_id=3)
            obj2.save()

            obj3,created = UserSocialAuth.objects.get_or_create(uid=email)
            obj3.user_id = obj.id
            obj3.provider = 'google-oauth2'
            obj3.extra_data = {'data':1}
            obj3.save()

            messages.success(request,'Your account has been created')
            return redirect('login2')


        return redirect('register')
    except Exception as e:
        obj = Exceptions(error_name = str(e))
        obj.save()
        return redirect('register')

def logout2(request):
    logout(request)
    return redirect('/')