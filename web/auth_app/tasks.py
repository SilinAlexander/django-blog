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


@app.task
def send_password_reset(**kwargs):
    print(kwargs)
    subject = 'Password reset'
    template = 'auth_app/email/password_reset_message.html'
    send_information_email(subject, template, kwargs.get('content'), [kwargs.get('to_email')])


def send_information_email(subject: str, template_name: str, content: dict, to_email: list):
    template = get_template(template_name=template_name)
    message = template.render(content)
    send_mail(subject=subject, message=message, from_email=None, recipient_list=to_email)
