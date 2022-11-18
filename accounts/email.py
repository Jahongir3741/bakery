from django.core.mail import send_mail, EmailMessage
from random import randint
from django.conf import settings
from .models import UserAccount


def send_code_email(my_email):
    subject = "Your account verification email"
    code = str(randint(1000, 9999))
    massage = f'Your code is {code}'
    from_email = settings.EMAIL_FROM_USER
    print(from_email)
    email = EmailMessage(
        subject=subject,
        body=massage,
        from_email=from_email,
        to=[my_email]
    )
    email.send()
    try:
        user_obj = UserAccount.objects.get(email=my_email)
        user_obj.code = code
        user_obj.save()
    except Exception as e:
        print(e)