# email_utils.py
import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def send_email(subject, body, to_email):
    creds = Credentials.from_authorized_user_file('token.pickle', ['https://www.googleapis.com/auth/gmail.send'])
    service = build('gmail', 'v1', credentials=creds)
    message = {
        'raw': base64.urlsafe_b64encode(f'Subject: {subject}\n\n{body}'.encode('utf-8')).decode('utf-8')
    }
    try:
        message = service.users().messages().send(userId='me', body=message).execute()
        print(f'Sent message to {to_email} Message Id: {message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')

# In your Django view or wherever you send emails
from django.http import HttpResponse
from .email_utils import send_email

def send_test_email(request):
    send_email('Test Subject', 'This is a test email body.', 'recipient@example.com')
    return HttpResponse('Email sent!')
