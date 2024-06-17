from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')


def activities(request):
    return render(request,'web/activities.html')

def donations(request):
    return render(request,'web/donations.html')

def counsellors(request):
    return render(request,'web/letMeet.html')


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
    return render(request,'web/articles.html')

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
    return render(request,'web/blog.html')


def register(request):
    return render(request,'web/register.html')

def failed2(request):
    messages.error(request,'You are not authorized')
    return render(request,'web/login.html')

@login_required
def profile(request):
    return render(request,'dashboard/dashboard.html')


def logout2(request):
    logout(request)
    return redirect('/')