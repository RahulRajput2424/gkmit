from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from email.message import EmailMessage
import smtplib

def send_email(subject,message,amount): 
    subject = subject
    message = "Dear User, your account has been {} with the ammount of {} and you current balance is {}".format(amount,message['data']['transaction_amount'],(message["Current Balance"]))
    from_email = "semwala12@gmail.com"

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['semwala12@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')