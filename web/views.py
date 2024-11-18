import datetime
import threading

from django.template.loader import render_to_string, get_template
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordContextMixin
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from sweetify import sweetify
from django.shortcuts import render, redirect

from .encryption_util import decrypt, encrypt
from user_management.models import User
from django.contrib import messages
import urllib
from django.contrib import messages
import json
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


from .models import *
from social_django.models import UserSocialAuth
from user_management.models import *
from verify_email.email_handler import send_verification_email
from django.utils.translation import gettext_lazy as _
# Create your views here.


from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _





class CustomPasswordResetView(PasswordContextMixin, FormView):
    email_template_name = "registration/password_reset_email.html"
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy("password_reset_done")
    template_name = "registration/password_reset_form.html"
    title = _("Password reset")
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        # Force the domain to use https://www.muditatribe.com
        opts = {
            "use_https": True,
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": {
                "domain": "www.muditatribe.com",  # Set the custom domain
                "protocol": "https",
            },
        }
        form.save(**opts)
        return super().form_valid(form)


def auth(request, token):
    if request.method == 'POST':
        # forgotPassword
        if token == 0:
            email = request.POST['email']
            msg = EmailMessage(
                "Mudita - Registration/Login App Password Reset",
                "To initiate the password reset process for your" + email +
                "Django Registration/Login App Account,click the link below:</br>"
                "https://muditatribe.gitam.edu/password_reset/" + email +
                "If clicking the link above doesn't work, please copy and paste the URL in a new browser window "
                "instead.</br></br> "
                "Sincerely,</br>"
                "The Mudita Team",
                'info@muditatribe.com',
                [email],
            )
            msg.content_subtype = "html"
            msg.send()
            messages.success(request,
                             "We've emailed you instructions for setting your password")
            return HttpResponseRedirect('/forgot/')
        # signUp
        if token == 1:
            form = SignUpForm(request.POST)
            try:

                if form.is_valid():
                    inactive_user = send_verification_email(request, form)
                    group_id = Group.objects.get(id=3)
                    obj, created = UserGroups.objects.get_or_create(group=group_id, user=inactive_user)
                    obj.group = group_id
                    obj.is_active = True
                    obj.is_default = True
                    obj.is_block = False
                    obj.save()
                    messages.success(request, "Successfully Registered")
                    return redirect('verify')
                else:
                    messages.error(request,"Unable to save your details. Try again")
                    return redirect('signup')
            except Exception as e:
                messages.error(request, str(e))
                return redirect('signup')

            messages.error(request,"Unable to save your details. Try again")
            return redirect('signup')


        # signIn
        if token == 2:
            form = signInForm(request.POST)

            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, "Invalid Email or password.")
            else:
                messages.error(request, "Invalid Email or password..")

        return redirect('signin')
    else:
        return redirect('signup')

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

def alternate_therapist(request):
    return render(request,'web/alternate.html')

def activities(request):
    return render(request,'web/activities.html')

def donations(request):
    return render(request,'web/donations.html')

def counsellors(request,paginate=None):
    data = User.objects.filter(userOf__group__name='counsellor')
    s = len(data)/12
    s = round(s)
    if paginate:
        paginate = decrypt(paginate)
        paginate = int(paginate)
        if paginate == 0:
            data = data[:12]
            current_page = 1

        elif paginate != 1 and paginate != 0:

            if paginate > s:
                paginate = s
                start = paginate - 1
                start = 12 * start
                p = paginate * 12
                data = data[start:p]
                current_page = paginate
            else:

                start = paginate - 1
                start = 12 * start
                p = paginate*12
                data = data[start:p]
                current_page = paginate
        else:
            data = data[:12]
            current_page = 1
    else:
        data = data[:12]
        current_page = 1

    pag = []
    for i in range(1,s+1):
        pag.append(i)
    print(pag)
    context=dict()
    context['data'] = data
    context['pag'] = pag
    context['current_page'] = current_page
    return render(request,'web/letMeet.html',context)

def forgot_password(request):
    try:
        email = request.POST['email']
        udata = User.objects.filter(email=email).last()
        send_password_reset_email(request,udata)
    except:
        messages.error(request,"Email does not exists!")
        return redirect('/login2')


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

def contactus(request):

    return render(request,'web/contact.html')

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


class AddMusic(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to="music/", null=True, blank=True)
    audio = models.FileField(upload_to="music/", null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    language = models.CharField(max_length=500,null=True,blank=True)
    music_type = models.CharField(max_length=500,null=True,blank=True)

    def admin_photo(self):
        if self.photo:
            return mark_safe('<img src="{}" width="100" />'.format(self.photo.url))
        else:
            return '(No photo)'
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True


def instrumental(request):

    return render(request,'web/instrumental.html')

def art(request):
    return render(request,'web/art.html')


def dance_class(request):
    youtube = AddVideo.objects.filter(youtube_vedio=True, video_type='dance')
    context = dict()
    context['youtube'] = youtube

    return render(request,'web/dance_class.html',context)

def music_class(request):
    data = AddMusic.objects.filter(music_type='Soothing Soundscapes')
    context = dict()
    context['data'] = data
    return render(request,'web/music_class.html',context)


def postural(request):
    youtube = AddVideo.objects.filter(youtube_vedio=True, video_type='postural')
    context = dict()
    context['youtube'] = youtube

    return render(request,'web/postural.html',context)


def sound_nature(request,id=None):
    if id:
        id = decrypt(id)
        adata = AddMusic.objects.filter(music_type="Sounds Of Nature")
        data = AddMusic.objects.filter(music_type="Sounds Of Nature",id=id).last()
    else:
        adata = AddMusic.objects.filter(music_type="Sounds Of Nature")
        data = AddMusic.objects.filter(music_type="Sounds Of Nature").last()
    context = dict()
    context['adata'] = adata
    context['data'] = data
    return render(request, 'web/sound_nature.html', context)

def smoothing_sound(request,id=None):
    if id:
        id = decrypt(id)
        adata = AddMusic.objects.filter(music_type="Soothing Soundscapes")
        data = AddMusic.objects.filter(music_type="Soothing Soundscapes",id=id).last()
    else:
        adata = AddMusic.objects.filter(music_type="Soothing Soundscapes")
        data = AddMusic.objects.filter(music_type="Soothing Soundscapes").last()
    context = dict()
    context['adata'] = adata
    context['data'] = data
    return render(request, 'web/calming.html', context)

class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = _("There is no user registered with the specified E-Mail address.")
            self.add_error('email', msg)

            print("not registered")
        return email

def signup(request):
    return render(request,'web/signup.html')

def verify(request):
    return render(request,'web/verify.html')

def verify_account(request,id):
    id = decrypt(id)
    obj = User.objects.get(id=id)
    if obj.is_active:
        messages.error(request, "Your account has been activated successfully.")
        return render(request,'link_expired.html')
    User.objects.filter(id=id).update(is_active=True)
    messages.success(request,"Your account has been activated successfully.")
    return redirect('/')

def articles(request,paginate=None):
    data = Articles.objects.filter(publish=True).exclude(article_type="mindful")
    s = len(data) / 6
    s = round(s)
    if paginate:
        paginate = decrypt(paginate)
        paginate = int(paginate)
        if paginate == 0:
            data = data[:6]
            current_page = 1

        elif paginate != 1 and paginate != 0:

            if paginate > s:
                paginate = s
                start = paginate - 1
                start = 6 * start
                p = paginate * 6
                data = data[start:p]
                current_page = paginate
            else:

                start = paginate - 1
                start = 6 * start
                p = paginate * 6
                data = data[start:p]
                current_page = paginate
        else:
            data = data[:6]
            current_page = 1
    else:
        data = data[:6]
        current_page = 1

    pag = []
    for i in range(1, s + 1):
        pag.append(i)
    print(pag)
    context = dict()
    context['data'] = data
    context['pag'] = pag
    context['current_page'] = current_page
    return render(request,'web/articles.html',context)



def mindful_articles(request):
    data = Articles.objects.filter(publish=True,article_type="mindful")
    context=dict()
    context['data'] = data
    return render(request,'web/mindful_articles.html',context)

def chants(request):
    return render(request,'web/chants.html')


def login2(request):
    return render(request,'web/login.html')

def user_login(request):
    return render(request,'web/user_login.html')





def check_user(request):
    email = request.POST.get('email')

    if not email:
        # If email is not provided, redirect to logout or handle error.
        return redirect('logout2')

    try:
        user = User.objects.get(username=email)
        group = user.groups.first()  # Fetch the first group if it exists.

        if group:
            request.session['gname'] = group.name  # Store the group name in the session.

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)

        return redirect('profile')
    except User.DoesNotExist:
        # Redirect to logout if user does not exist.
        return redirect('logout2')


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

def send_password_reset_email(requset,user):
    s_email = user.email
    s_id = encrypt(user.id)
    username = encrypt(user.username)

    context = dict()
    context['id'] = s_id
    context['username'] = username
    email_list = [s_email]


    message = get_template('emails/password_reset.html').render(context)
    msg = EmailMessage(
        'Password reset on muditatribe.com',
        message,
        'noreply@muditatribe.com',
        email_list
    )
    msg.content_subtype = "html"
    EmailThread(msg).start()

    return 1


def send_verification_email_custom(requset,user):
    s_email = user.email
    s_id = encrypt(user.id)

    context = dict()
    context['id'] = s_id
    email_list = [s_email]


    message = get_template('emails/verify_email.html').render(context)
    msg = EmailMessage(
        'Email Verification Mail - Mudita Tribe',
        message,
        'noreply@muditatribe.com',
        email_list
    )
    msg.content_subtype = "html"
    EmailThread(msg).start()

    return 1


def add_new_user(request):
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
            if request.method == 'POST':
                uname = request.POST.get('uname')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                password = request.POST.get('password')
                rpassword = request.POST.get('rpassword')

                # Form validation
                if not uname or not email or not phone or not password or not rpassword:
                    messages.error(request, "All fields are required.")
                    return redirect('signup')

                if password != rpassword:
                    messages.error(request, "Passwords do not match.")
                    return redirect('signup')

                try:
                    validate_email(email)
                except ValidationError:
                    messages.error(request, "Enter a valid email address.")
                    return redirect('signup')

                if User.objects.filter(username=uname).exists():
                    messages.error(request, "Username already exists.")
                    return redirect('signup')

                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists.")
                    return redirect('signup')

                # Create user
                user = User.objects.create_user(username=email,first_name=uname, email=email,phone=phone, password=password)
                user.is_active = False
                user.save()

                obj2, created = UserGroups.objects.get_or_create(user_id=user.id, group_id=3)
                obj2.is_active = True
                obj2.is_default = True
                obj2.is_block = False
                obj2.save()

                send_verification_email_custom(request, user)

                return redirect('verify')
        else:
            messages.error(request, "Please Enter Captcha!")
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'web/signup.html')
    except Exception as e:
        messages.error(request, str(e))
        return render(request, 'web/signup.html')

def password_reset_confirm(request,id):
    id = decrypt(id)
    context = dict()
    context['id'] = id
    return render(request,'web/password_reset_confirm.html',context)


def login_user(request):
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
            if request.method == 'POST':
                email_or_username = request.POST.get('email')
                password = request.POST.get('password')

                # Authenticate user
                user = authenticate(request, username=email_or_username, password=password)

                if user is None:
                    # If the username is an email, try to authenticate with email
                    try:
                        user = authenticate(request, username=None, password=password, email=email_or_username)
                    except Exception as e:
                        messages.error(request, "Invalid username/email or password.")
                        return redirect('login2')

                if user is not None:
                    login(request, user)

                    return redirect('profile')  # Redirect to dashboard or another page

                messages.error(request, "Invalid username/email or password.")
                return redirect('login2')
        else:
            messages.error(request, 'Please Enter Captcha!')
            return redirect(request.META.get('HTTP_REFERER'))

        return render(request, 'web/login.html')
    except:
        return render(request, 'web/login.html')


def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def get_category_data(request):
    category = request.GET.get('category')
    data = ''
    if category == 'activities':
        data = AddVideo.objects.filter(youtube_vedio=True).values('id','name')
        data = list(data)

    if category == 'mindful':
        data = Articles.objects.filter(article_type='mindful').values('id','title')
        data = list(data)
        for i in range(len(data)):
            data[i]['name'] = data[i]['title']

    if category == 'articles':
        data = Articles.objects.all().values('id','title')
        data = list(data)
        for i in range(len(data)):
            data[i]['name'] = data[i]['title']

    if category == 'blogs':
        data = Blog.objects.all().values('id','title')
        data = list(data)
        for i in range(len(data)):
            data[i]['name'] = data[i]['title']

    if category == 'counsellors':
        data = User.objects.filter(userOf__group__name='counsellor').values('id','first_name','expertise')
        data = list(data)
        for i in range(len(data)):
            data[i]['name'] = str(data[i]['first_name']) + ' - ' + str(data[i]['expertise'])
    if category == 'helplines':
        data = AddHelpline.objects.all().values('id','name')
        data = list(data)
    return JsonResponse({'data':data})


def search_result(request):
    category = request.POST.get('category')
    search_value = request.POST.get('search_value')
    data = ''
    if category == 'activities':
        data = AddVideo.objects.filter(youtube_vedio=True,id=search_value).last()


    if category == 'mindful':
        return redirect('article_details',encrypt(search_value))


    if category == 'articles':
        return redirect('article_details',encrypt(search_value))


    if category == 'blogs':
        return redirect('blog_details',encrypt(search_value))

    if category == 'counsellors':
        data = User.objects.filter(userOf__group__name='counsellor',id=search_value).last()

    if category == 'helplines':
        data = AddHelpline.objects.filter(id=search_value).last()

    context = dict()
    context['data'] = data
    context['category'] = category
    return render(request,'web/search_results.html',context)





def music_details(request,id):
    id = decrypt(id)
    data = AddMusic.objects.get(id=id)
    adata = AddMusic.objects.all()
    return render(request,'web/music_d.html',{'data':data,'adata':adata})

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

def article_details(request,id):
    id = decrypt(id)
    data = Articles.objects.get(id=id)
    context = dict()
    context['data'] = data
    return render(request,'web/article_details.html',context)




def blog_details(request,id):
    id = decrypt(id)
    data = Blog.objects.get(id=id)
    context = dict()
    context['data'] = data
    return render(request,'web/blog_details.html',context)


import threading


from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
# Create your views here.
from django.template.loader import get_template
from sweetify import sweetify
import urllib
import json
from django.conf import settings

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


from .models import *

def submit_form(request):
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
            if request.method == 'POST':
                name = request.POST['name']
                phone = request.POST['phone']
                gender = request.POST.get('gender', '')
                email = request.POST['email']
                dob = request.POST['dob']
                city = request.POST['city']
                profession = request.POST['profession']
                specialisation = request.POST['specialisation']
                experience = request.POST['experience']
                delivery_mode = request.POST['delivery_mode']
                description = request.POST['description']
                message = request.POST['message']

                cv = request.FILES['cv']
                degree = request.FILES['degree']
                photo = request.FILES['photo']

                new_professional = MentalHealthProfessional(
                    name=name,
                    phone=phone,
                    gender=gender,
                    email=email,
                    dob=dob,
                    city=city,
                    profession=profession,
                    specialisation=specialisation,
                    experience=experience,
                    delivery_mode=delivery_mode,
                    description=description,
                    message=message,
                    cv=cv,
                    degree=degree,
                    photo=photo
                )
                new_professional.save()
                sweetify.success(request,'successfully submitted')
        else:
            messages.error(request, 'Please Enter Captcha!')
            return redirect(request.META.get('HTTP_REFERER'))
        return redirect('professional')  # Replace 'success_page' with your success URL name
    except:
        return render(request, 'professional')  # Replace 'form_page.html' with your form template name

def submit_form2(request):
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
            if request.method == 'POST':
                name = request.POST['name']
                phone = request.POST['phone']
                gender = request.POST.get('gender', '')
                email = request.POST['email']
                dob = request.POST['dob']
                city = request.POST['city']
                specialisation = request.POST['specialisation']
                experience = request.POST['experience']
                delivery_mode = request.POST['delivery_mode']
                description = request.POST['description']
                message = request.POST['message']

                cv = request.FILES['cv']
                degree = request.FILES['degree']
                photo = request.FILES['photo']

                new_professional = MentalHealthVolunteer(
                    name=name,
                    phone=phone,
                    gender=gender,
                    email=email,
                    dob=dob,
                    city=city,

                    specialisation=specialisation,
                    experience=experience,
                    delivery_mode=delivery_mode,
                    description=description,
                    message=message,
                    cv=cv,
                    degree=degree,
                    photo=photo
                )
                new_professional.save()
                messages.success(request,'successfully submitted')
                return redirect('volunteer')  # Replace 'success_page' with your success URL name
        else:
            messages.error(request, 'Please Enter Captcha!')
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'volunteer')  # Replace 'form_page.html' with your form template name
    except:
        return render(request, 'volunteer')  # Replace 'form_page.html' with your form template name


def submit_form3(request):
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
            if request.method == 'POST':
                name = request.POST['name']
                phone = request.POST['phone']
                gender = request.POST.get('gender', '')
                email = request.POST['email']
                dob = request.POST['dob']
                city = request.POST['city']
                specialisation = request.POST['specialisation']
                experience = request.POST['experience']
                delivery_mode = request.POST['delivery_mode']
                description = request.POST['description']
                message = request.POST['message']

                cv = request.FILES['cv']
                degree = request.FILES['degree']
                photo = request.FILES['photo']

                new_professional = AlternateTherapist(
                    name=name,
                    phone=phone,
                    gender=gender,
                    email=email,
                    dob=dob,
                    city=city,

                    specialisation=specialisation,
                    experience=experience,
                    delivery_mode=delivery_mode,
                    description=description,
                    message=message,
                    cv=cv,
                    degree=degree,
                    photo=photo
                )
                new_professional.save()
                messages.success(request,'successfully submitted')
                return redirect('alternate_therapist')  # Replace 'success_page' with your success URL name
        else:
            messages.error(request, 'Please Enter Captcha!')
            return redirect(request.META.get('HTTP_REFERER'))
        return render(request, 'alternate_therapist')  # Replace 'form_page.html' with your form template name
    except:
        return render(request, 'alternate_therapist')  # Replace 'form_page.html' with your form template name





def add_contact(request):
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

        if result.get('success'):
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            context=dict()
            context['name'] = name
            context['email'] = email
            context['phone'] = phone
            context['message'] = message



            email_list = ['lakshminarayanateku@gmail.com']

            message = get_template('emails/contact.html').render(context)
            msg = EmailMessage(
                'New contact added: ' + name,
                message,
                'noreply@muditatribe.com',
                email_list

            )
            msg.content_subtype = "html"
            EmailThread(msg).start()

            obj = Contact(name=name, email=email, phone=phone, description=message)
            obj.save()

            messages.success(request, 'Thank you! We will contact you soon.')
            return redirect('/')
        else:
            messages.error(request, 'Please complete the CAPTCHA.')
            return redirect(request.META.get('HTTP_REFERER'))
    except urllib.error.URLError as e:
        messages.error(request, 'There was an error processing your request. Please try again later.')
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        messages.error(request, e)
        return redirect(request.META.get('HTTP_REFERER'))


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string


from user_management.models import User


def get_counsellor_data(request):
    id = request.GET.get('id')
    data = User.objects.get(id=id)

    context = dict()
    context['data'] = data
    html_form = render_to_string('web/counsellor_data.html', context, request=request)

    return JsonResponse({'html_form': html_form})


def get_counsellor(request,id):
    id = decrypt(id)
    data = User.objects.get(id=id)

    context = dict()
    context['data'] = data
    return render(request,'dashboard/get_appointment.html')

@login_required
def counsellors_list(request):

    data = User.objects.filter(userOf__group__name='counsellor')

    context = dict()
    context['data'] = data


    return render(request,'dashboard/counsellor_list.html',context)



from datetime import datetime
import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
from .models import Payment
import sweetify
from django.shortcuts import render, redirect
import json
import razorpay
# Create your views here.
from django.views.decorators.csrf import csrf_exempt



from django.shortcuts import render, redirect

# Create your views here.
from sweetify import sweetify
import urllib
from django.contrib import messages
import json
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

today = datetime.now().date()
current_time = datetime.now().time()

import json
import hmac
import hashlib

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import threading

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        # pass
        # self.email.send()
        self.email.send(fail_silently=False)


def send_donation_receipt(donor_name, email, amount_paid, payment_method, razorpay_order_id,razorpay_payment_id, paid_date):
    subject = 'Thank You for Your Donation!'
    organization_name = 'Mudita Tribe'
    support_email = 'info@mudita.com'
    bcc_email = 'teku.lakshminarayana@gmail.com'
    year = datetime.now().year


    context = {
        'donor_name': donor_name,
        'organization_name': organization_name,
        'amount_paid': amount_paid,
        'payment_method': payment_method,
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': razorpay_payment_id,
        'paid_date': paid_date.date(),
        'support_email': support_email,
        'year': year,
    }
    email_list = [email]


    message = get_template('emails/donation_receipt.html').render(context)
    msg = EmailMessage(
        'Thank You for Your Donation!',
        message,
        'noreply@muditatribe.com',
        email_list,
        bcc=[bcc_email]
    )
    msg.content_subtype = "html"
    EmailThread(msg).start()

    return 1

@csrf_exempt
@require_POST
def webhook_razorpay(request):
    webhook_secret = settings.RAZORPAY_WEBHOOK_SECRET
    received_signature = request.headers.get('X-Razorpay-Signature')
    payload = request.body

    # Verify the signature
    expected_signature = hmac.new(webhook_secret.encode(), payload, hashlib.sha256).hexdigest()
    if received_signature != expected_signature:
        return JsonResponse({'status': 'failed', 'message': 'Invalid signature'}, status=400)

    event = json.loads(payload)
    event_type = event.get('event')

    if event_type == 'payment.captured':
        payment_id = event['payload']['payment']['entity']['id']
        try:
            payment = DonatedUser.objects.get(razorpay_order_id=payment_id)
            payment.status = 'Paid'
            payment.paid_date = datetime.now()
            payment.paid = True


            payment.save()
        except:
            pass


        # Process the payment captured event
        # Update your database or perform other actions based on the payment ID

        return JsonResponse({'status': 'success', 'message': 'Payment captured processed'})

    # Handle other event types if needed

    return JsonResponse({'status': 'success', 'message': 'Event processed'})



def payment(request):
    return render(request,'web/initiate_payment.html')

def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST.get('amount')) * 100  # Convert to paisa

        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'
        })

        payment_obj = Payment(
            razorpay_order_id=payment['id'],
            amount=amount / 100
        )
        payment_obj.save()

        context = {
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'amount': amount,
            'order_id': payment['id']
        }

        return render(request, 'web/payment.html', context)

    return render(request, 'initiate_payment.html')


def payment_cancel(request):
    messages.error(request,"Payment Failed")
    return render(request,'web/payment_failed.html')

@csrf_exempt
def payment_success(request):
    try:
        if request.method == "POST":
            data = request.POST
            order_id = data.get('razorpay_order_id')
            payment_id = data.get('razorpay_payment_id')
            signature = data.get('razorpay_signature')
            payment_method = data.get('payment_method')
            txn_id = data.get('txn_id')
            amount_paid = data.get('amount')  # Capture the amount paid

            payment = DonatedUser.objects.get(razorpay_order_id=order_id)
            payment.razorpay_payment_id = payment_id
            payment.razorpay_signature = signature
            payment.payment_type = payment_method
            payment.txn_id = txn_id
            payment.paid_amount = int(amount_paid)/100  # Save the amount paid

            # Verify the payment signature
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })

            payment.status = 'Paid'
            payment.paid = True
            payment.paid_date = datetime.now()
            payment.save()
            amount_paid = int(amount_paid)/100
            send_donation_receipt(payment.name, payment.email, amount_paid, payment_method, payment.razorpay_order_id,payment.razorpay_payment_id, payment.paid_date)

            messages.success(request, "Payment Successful! Thank you for your donation.")

        return render(request, 'web/payment_success.html')

    except Exception as e:
        print("error")
        print(e)
        print("error")
        return redirect('donations')


def add_donation(request):
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
            name = request.POST['uname']
            address = request.POST['address']
            email = request.POST['email']
            indian = request.POST.get('indian',False)
            # payment = request.POST['payment']

            amount = int(request.POST['amount'])
            # if amountDropdown == "custom":
            #     amount = int(request.POST['amount'])
            # else:
            #     amount = int(amountDropdown)
            phone = request.POST['phone']
            try:
                pan_card = request.FILES['pan']
            except:
                pan_card = ""
            import requests

            amount = amount * 100
            payment = client.order.create({
                'amount': amount,
                'currency': 'INR',
                'payment_capture': '1'
            })

            lamount = amount / 100

            payment_obj = DonatedUser(amount=str(lamount),
            name=name,
            email = email,
            address = address,
            phone = phone,
            razorpay_order_id = payment['id']
            )
            if indian:
                payment_obj.indian_citizen = True
            if pan_card:
                payment_obj.pan_card = pan_card
            payment_obj.save()

            context = {
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'amount': amount,
                'order_id': payment['id']
            }
            return render(request,'web/payment.html',context)
            # if payment == "bank":
            #     messages.success(request, 'Thank you for your donation!')
            #     return render(request,'web/bank_details.html')
            # if payment == "upi":
            #     messages.success(request, 'Thank you for your donation! Please scan the QR Code below')
            #     return render(request,'web/upi.html')
            # if payment == "credit":
            #     messages.success(request, 'Thank you for your donation')
            #     return render(request,'web/credit.html')
        else:
            messages.error(request,"Please Enter Captcha!")
            return redirect(request.META.get('HTTP_REFERER'))


    except Exception as e:
        print(e)
        messages.error(request,'something went wrong')
        return redirect('donations')

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
