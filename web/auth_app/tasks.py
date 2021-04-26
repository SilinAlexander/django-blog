from django.template.loader import get_template

from src.celery import app
from django.core.mail import send_mail


@app.task
def send_verify_email(**kwargs):
    subject = 'Confirm your email address'
    template = get_template('auth_app/email/confirm_email_massage.html')
    message = template.render(kwargs.get('content'))
    print(kwargs)
    send_mail(subject=subject, message=message, from_email=None, recipient_list=[kwargs.get('to_email')])
