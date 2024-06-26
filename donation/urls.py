
from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_donation',add_donation, name='add_donation'),

    path('payment',payment, name='payment'),
    path('payment_success',payment_success, name='payment_success'),
    path('initiate_payment',initiate_payment, name='initiate_payment'),


]
