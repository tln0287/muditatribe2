import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from sweetify import sweetify

from article.models import Articles
from blog.models import Blog
from counsellor.encryption_util import decrypt
from helplines.models import AddHelpline
from music.models import AddMusic
from testimonial.models import UserTestimonial
from vedios.models import AddVideo
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

def glossary(request):
    return render(request,'web/glossary.html')

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


@login_required
def user_support(request):
    if request.user.groups.filter(name="Admin"):
        qdata = UserSupport.objects.all()
    else:
        qdata = UserSupport.objects.filter(user__u_id=request.user.u_id).all()
    context = dict()
    context['qdata'] = qdata
    return render(request, 'support/user_support.html', context)

@login_required
def add_new_ticket(request):
    try:
        title = request.POST['title']
        comments = request.POST['comments']
        qdoc = request.FILES.get('qdoc', False)
        user_d = User.objects.get(id=request.user.id)
        obj = UserSupport(user=user_d, title=title)
        obj.save()
        if qdoc:
            obj_new = UserSupportComment(user=user_d, support_id=obj.id, comments=comments, file=qdoc)
        else:
            obj_new = UserSupportComment(user=user_d, support_id=obj.id, comments=comments)
        obj_new.save()
        sweetify.success(request, 'Successfully Saved Your Ticket')
    except:
        sweetify.error(request, 'Unable to save your query contact gresignation_support@gitam.edu')
    return redirect(request.META.get('HTTP_REFERER'))



@login_required
def view_qcomments(request, id):
    id = decrypt(id)
    qstatus = UserSupport.objects.get(id=id)
    qcomments = UserSupportComment.objects.filter(support_id=id).all()
    context = dict()
    context['qdata'] = qcomments
    context['qid'] = id
    context['qstatus'] = qstatus.query_status
    return render(request, 'support/query_comments.html', context)

@login_required
def delete_query(request, id):
    id = decrypt(id)
    UserSupport.objects.get(id=id).delete()
    sweetify.success(request, 'Successfully Deleted Your Ticket')
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def add_qcomments(request):
    comments = request.POST['comments']
    id = request.POST['qid']
    if request.user.groups.filter(name="Admin").exists():
        UserSupport.objects.filter(id=id).update(reply_status=1)
    else:
        UserSupport.objects.filter(id=id).update(reply_status=0)
    obj = UserSupportComment(support_id=id, user_id=request.user.id, comments=comments)
    obj.save()
    sweetify.success(request, 'Successfully Saved Your Ticket')
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def close_ticket(request):
    qid = request.GET.get('qid')
    UserSupport.objects.filter(id=qid).update(query_status=1)
    return JsonResponse({"data": 1})

def contact(request):

    return render(request,'web/joinTheTribe.html')

def breathing(request):
    youtube = AddVideo.objects.filter(youtube_vedio=True, video_type='Breathing')
    context = dict()
    context['youtube'] = youtube
    return render(request, 'web/breathing.html', context)


def guided_meditation(request):
    youtube = AddVideo.objects.filter(youtube_vedio=True,video_type='Guided Meditation')
    context = dict()
    context['youtube'] = youtube
    return render(request,'web/meditation.html',context)

def music(request):
    data = AddMusic.objects.all()
    context = dict()
    context['data'] = data
    return render(request,'web/music.html',context)

def instrumental(request):
    data = AddMusic.objects.all()
    context = dict()
    context['data'] = data
    return render(request,'web/instrumental.html',context)

def art(request):
    return render(request,'web/art.html')


def dance_class(request):
    youtube = AddVideo.objects.filter(youtube_vedio=True, video_type='dance')
    context = dict()
    context['youtube'] = youtube

    return render(request,'web/dance_class.html',context)

def music_class(request):
    data = AddMusic.objects.filter(music_type='calming')
    context = dict()
    context['data'] = data
    return render(request,'web/music_class.html',context)


def postural(request):
    youtube = AddVideo.objects.filter(youtube_vedio=True, video_type='postural')
    context = dict()
    context['youtube'] = youtube

    return render(request,'web/postural.html',context)


def sound_nature(request):
    data = AddMusic.objects.all()
    context = dict()
    context['data'] = data
    return render(request, 'web/sound_nature.html', context)



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
    data = AddMusic.objects.all()
    context = dict()
    context['data'] = data
    return render(request,'web/music.html',context)



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

@login_required
def user_blog(request):
    data = Blog.objects.filter(user_id=request.user.id)
    context = dict()
    context['data'] = data
    return render(request,'dashboard/blog.html',context)

@login_required
def add_user_blog(request):
    title = request.POST['title']
    content = request.POST['content']
    image = request.FILES['image']
    obj, created = Blog.objects.get_or_create(created_by=request.user.first_name,title=title)
    obj.content = content
    obj.blog_main_image = image
    obj.user_id = request.user.id
    obj.blog_date = datetime.datetime.now().date()
    obj.save()
    sweetify.success(request,"Blog added successfully")
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_blog(request,id):
    id = decrypt(id)
    Blog.objects.filter(id=id).delete()
    sweetify.success(request, "Blog deleted successfully")
    return redirect(request.META.get('HTTP_REFERER'))

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