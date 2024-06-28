
from django.urls import path, include
from .views import *

urlpatterns = [
    path('blog_details/<str:id>',blog_details, name='blog_details'),
]