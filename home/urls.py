
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('about',about, name='about'),
    path('activities',activities, name='activities'),
    path('donations',donations, name='donations'),
    path('counsellors',counsellors, name='counsellors'),
    path('contact',contact, name='contact'),
    path('breathing',breathing, name='breathing'),
    path('music',music, name='music'),
    path('music_class',music_class, name='music_class'),
    path('art',art, name='art'),
    path('login2',login2, name='login2'),
    path('guided_meditation',guided_meditation, name='guided_meditation'),
    path('postural',postural, name='postural'),
    path('sound_nature',sound_nature, name='sound_nature'),
    path('dance_class',dance_class, name='dance_class'),
    path('failed2',failed2, name='failed2'),
    path('articles',articles, name='articles'),
    path('chants',chants, name='chants'),
    path('music_article',music_article, name='music_article'),
    path('privacy_policy',privacy_policy, name='privacy_policy'),
    path('terms_conditions',terms_conditions, name='terms_conditions'),
    path('refund',refund, name='refund'),
    path('register',register, name='register'),
    path('blog',blog, name='blog'),
    path('profile',profile,name='profile'),
    path('logout2',logout2,name='logout2'),

]
