
from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_donation',add_donation, name='add_donation'),
    path('webhook_razorpay',webhook_razorpay, name='webhook_razorpay'),

    path('payment',payment, name='payment'),
    path('payment_success',payment_success, name='payment_success'),
    path('payment_cancel',payment_cancel, name='payment_cancel'),
    path('initiate_payment',initiate_payment, name='initiate_payment'),


]
