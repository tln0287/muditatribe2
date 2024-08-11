
from django.urls import path, include
from .views import *

urlpatterns = [

    path('add_contact',add_contact, name='add_contact'),
    path('submit_form',submit_form, name='submit_form'),
    path('submit_form2',submit_form2, name='submit_form2'),
    path('submit_form3',submit_form3, name='submit_form3'),


]
