
from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_testimonial',add_testimonial, name='add_testimonial'),


]
