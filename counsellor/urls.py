
from django.urls import path, include
from .views import *

urlpatterns = [
 path('get_counsellor_data',get_counsellor_data,name="get_counsellor_data"),
]

