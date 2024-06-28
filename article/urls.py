
from django.urls import path, include
from .views import *

urlpatterns = [
    path('article_details/<str:id>',article_details, name='article_details'),
]