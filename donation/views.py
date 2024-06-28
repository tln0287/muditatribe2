from datetime import datetime
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
from .models import Payment
import sweetify
from django.shortcuts import render, redirect
import json
import razorpay
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from donation.models import *
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

today = datetime.now().date()
current_time = datetime.now().time()


def payment(request):
    return render(request,'web/initiate_payment.html')

def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST.get('amount')) * 100  # Convert to paisa

        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'
        })

        payment_obj = Payment(
            razorpay_order_id=payment['id'],
            amount=amount / 100
        )
        payment_obj.save()

        context = {
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'amount': amount,
            'order_id': payment['id']
        }

        return render(request, 'web/payment.html', context)

    return render(request, 'initiate_payment.html')


@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        data = request.POST
        order_id = data.get('razorpay_order_id')
        payment_id = data.get('razorpay_payment_id')
        signature = data.get('razorpay_signature')
        payment = DonatedUser.objects.get(razorpay_order_id=order_id)
        payment.razorpay_payment_id = payment_id
        payment.razorpay_signature = signature

        client.utility.verify_payment_signature({
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        })

        payment.status = 'Paid'
        payment.paid = True
        payment.save()

        return render(request, 'web/payment_success.html')

    return redirect('initiate_payment')


def add_donation(request):
    try:
        name = request.POST['uname']
        address = request.POST['address']
        email = request.POST['email']
        amount = int(request.POST['amount'])
        phone = request.POST['phone']
        pan_card = request.FILES['pan']
        import requests
        import json
        amount = amount * 100
        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'
        })
        lamount = amount / 100

        payment_obj = DonatedUser(
        razorpay_order_id=payment['id'],
        amount=str(lamount),
        name=name,
        email = email,
        address = address,
        phone = phone,
        pan_card = pan_card
        )
        payment_obj.save()

        context = {
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'amount': amount,
            'order_id': payment['id']
        }

        return render(request,'web/payment.html',context)
    except Exception as e:
        print(e)
        sweetify.error(request,'something went wrong')
        return redirect('donations')

