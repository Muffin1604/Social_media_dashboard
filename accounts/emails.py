from django.core.mail import send_mail
import random
from django.conf import settings
from .models import CustomUser

def send_otp(email):
    subject = f'd'
    otp = random.randint(1000,9999)
    message = f'{otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj = CustomUser.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
