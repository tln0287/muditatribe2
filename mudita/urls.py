"""
URL configuration for mudita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.views.static import serve

admin.site.site_header = "Mudita Tribe"
admin.site.site_title = "Mudita Tribe"

urlpatterns = [
     re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('contact.urls')),
    path('', include('donation.urls')),
    path('', include('testimonial.urls')),
    path('', include('counsellor.urls')),
    path('', include('blog.urls')),
    path('', include('article.urls')),
    path('', include('helplines.urls')),
    path('', include('music.urls')),
    path('', include('vedios.urls')),
path('', include('social_django.urls', namespace='social')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
