

from django.urls import path, include
from .views import *

urlpatterns = [
 path('get_helpline_data',get_helpline_data,name="get_helpline_data"),
]

