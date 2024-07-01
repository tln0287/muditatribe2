

from django.urls import path, include
from .views import *

urlpatterns = [
 path('music-details/<str:id>',music_details,name="music-details")
]

