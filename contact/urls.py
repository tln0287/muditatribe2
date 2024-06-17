
from django.urls import path, include
from .views import *

urlpatterns = [

    path('add_contact',add_contact, name='add_contact'),


]
