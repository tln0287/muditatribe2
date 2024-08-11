from datetime import datetime
import json
from django.contrib import messages
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

from django.shortcuts import render, redirect

# Create your views here.
from sweetify import sweetify
import urllib
from django.contrib import messages
import json
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

today = datetime.now().date()
current_time = datetime.now().time()

import json
import hmac
import hashlib

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import threading

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        # pass
        # self.email.send()
        self.email.send(fail_silently=False)


def send_donation_receipt(donor_name, email, amount_paid, payment_method, razorpay_order_id, paid_date):
    subject = 'Thank You for Your Donation!'
    organization_name = 'Mudita Tribe'
    support_email = 'info@mudita.com'
    bcc_email = 'teku.lakshminarayana@gmail.com'
    year = datetime.now().year


    context = {
        'donor_name': donor_name,
        'organization_name': organization_name,
        'amount_paid': amount_paid,
        'payment_method': payment_method,
        'razorpay_order_id': razorpay_order_id,
        'paid_date': paid_date.date(),
        'support_email': support_email,
        'year': year,
    }
    email_list = [email]


    message = get_template('emails/donation_receipt.html').render(context)
    msg = EmailMessage(
        'Thank You for Your Donation!',
        message,
        'admin@muditatribe.com',
        email_list,
        bcc=[bcc_email]
    )
    msg.content_subtype = "html"
    EmailThread(msg).start()

    return 1

@csrf_exempt
@require_POST
def webhook_razorpay(request):
    webhook_secret = settings.RAZORPAY_WEBHOOK_SECRET
    received_signature = request.headers.get('X-Razorpay-Signature')
    payload = request.body

    # Verify the signature
    expected_signature = hmac.new(webhook_secret.encode(), payload, hashlib.sha256).hexdigest()
    if received_signature != expected_signature:
        return JsonResponse({'status': 'failed', 'message': 'Invalid signature'}, status=400)

    event = json.loads(payload)
    event_type = event.get('event')

    if event_type == 'payment.captured':
        payment_id = event['payload']['payment']['entity']['id']
        try:
            payment = DonatedUser.objects.get(razorpay_order_id=payment_id)
            payment.status = 'Paid'
            payment.paid_date = datetime.now()
            payment.paid = True


            payment.save()
        except:
            pass


        # Process the payment captured event
        # Update your database or perform other actions based on the payment ID

        return JsonResponse({'status': 'success', 'message': 'Payment captured processed'})

    # Handle other event types if needed

    return JsonResponse({'status': 'success', 'message': 'Event processed'})



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


def payment_cancel(request):
    messages.error(request,"Payment Failed")
    return render(request,'web/payment_failed.html')

@csrf_exempt
def payment_success(request):
    try:
        if request.method == "POST":
            data = request.POST
            order_id = data.get('razorpay_order_id')
            payment_id = data.get('razorpay_payment_id')
            signature = data.get('razorpay_signature')
            payment_method = data.get('payment_method')
            txn_id = data.get('txn_id')
            amount_paid = data.get('amount')  # Capture the amount paid

            payment = DonatedUser.objects.get(razorpay_order_id=order_id)
            payment.razorpay_payment_id = payment_id
            payment.razorpay_signature = signature
            payment.payment_type = payment_method
            payment.txn_id = txn_id
            payment.paid_amount = int(amount_paid)/100  # Save the amount paid

            # Verify the payment signature
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })

            payment.status = 'Paid'
            payment.paid = True
            payment.paid_date = datetime.now()
            payment.save()
            send_donation_receipt(payment.name, payment.email, amount_paid, payment_method, payment.razorpay_order_id, payment.paid_date)

            messages.success(request, "Payment Successful! Thank you for your donation.")

        return render(request, 'web/payment_success.html')
        messages.error(request, "Payment Failed. Try again")

        return redirect('initiate_payment')
    except Exception as e:
        print("error")
        print(e)
        print("error")
        return redirect('donations')


def add_donation(request):
    try:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success']:
            name = request.POST['uname']
            address = request.POST['address']
            email = request.POST['email']
            indian = request.POST.get('indian',False)
            # payment = request.POST['payment']

            amount = int(request.POST['amount'])
            # if amountDropdown == "custom":
            #     amount = int(request.POST['amount'])
            # else:
            #     amount = int(amountDropdown)
            phone = request.POST['phone']
            try:
                pan_card = request.FILES['pan']
            except:
                pan_card = ""
            import requests

            amount = amount * 100
            payment = client.order.create({
                'amount': amount,
                'currency': 'INR',
                'payment_capture': '1'
            })

            lamount = amount / 100

            payment_obj = DonatedUser(amount=str(lamount),
            name=name,
            email = email,
            address = address,
            phone = phone,
            razorpay_order_id = payment['id']
            )
            if indian:
                payment_obj.indian_citizen = True
            if pan_card:
                payment_obj.pan_card = pan_card
            payment_obj.save()

            context = {
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'amount': amount,
                'order_id': payment['id']
            }
            return render(request,'web/payment.html',context)
            # if payment == "bank":
            #     messages.success(request, 'Thank you for your donation!')
            #     return render(request,'web/bank_details.html')
            # if payment == "upi":
            #     messages.success(request, 'Thank you for your donation! Please scan the QR Code below')
            #     return render(request,'web/upi.html')
            # if payment == "credit":
            #     messages.success(request, 'Thank you for your donation')
            #     return render(request,'web/credit.html')
        else:
            messages.error(request,"Please Enter Captcha!")
            return redirect(request.META.get('HTTP_REFERER'))


    except Exception as e:
        print(e)
        messages.error(request,'something went wrong')
        return redirect('donations')

