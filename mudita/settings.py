"""
Django settings for mudita project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wj=mn_^x2cnt4_v+ow=h%xj!-gg_=q6kjz3mwx547o^tc1h@9k'

ENCRYPT_KEY = b'gOO5zRy11u0LutYE9sZPLEtgJLBVqz5fXveYoU3Uh3I='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

GOOGLE_RECAPTCHA_SECRET_KEY = '6LeQbhgqAAAAAOgvpSoUdD7yCk5ugvagYx-l-Ley'

RAZORPAY_KEY_ID = 'rzp_test_qbKX3UuZ1StKj1'
RAZORPAY_KEY_SECRET = '7ycHLJComxHxWNI3CuNLSRRW'
RAZORPAY_WEBHOOK_SECRET = 'Mudita@2024'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'home',
    'contact',
    'donation',
    'testimonial',
    'usermanagement',
    'social_django',
    'django_social_share',
    'counsellor',
    'blog',
    'helplines',
    'mindfulTradition',
    'sweetify',
    'tinymce',
    'article',
    'music',
    'vedios',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
'social_django.middleware.SocialAuthExceptionMiddleware',
]

TINYMCE_DEFAULT_CONFIG = {
    'image_dimensions': False,
    "plugins": """
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            """,
    "toolbar1": """
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            """,
    "toolbar2": """
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            """,
    "contextmenu": "formats | link image",
    "menubar": True,
    "statusbar": True,
}

ROOT_URLCONF = 'mudita.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'customtag': 'templatetags.customtag',
            },
        },
    },
]

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail

    'social_core.backends.google.GoogleOAuth2',

]

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {'prompt': 'select_account'}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '44023736936-94dmn405b2ebqraml0hq9tvcido59tdj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_ON_GET = True

SOCIAL_AUTH_URL_NAMESPACE = 'social'


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'auth.pipeline.get_user',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (

    'social_core.pipeline.disconnect.get_entries',

    'social_core.pipeline.disconnect.revoke_tokens',

    'social_core.pipeline.disconnect.disconnect',
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'admin@muditatribe.com'
EMAIL_HOST_PASSWORD = 'Mudita2022'
EMAIL_PORT = 587

WSGI_APPLICATION = 'mudita.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'mudita',
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Correct time zone
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


AUTH_USER_MODEL = 'usermanagement.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/profile'
LOGIN_URL = '/profile'
LOGOUT_REDIRECT_URL='/logout2'

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
