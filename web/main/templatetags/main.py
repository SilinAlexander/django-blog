from datetime import datetime, timedelta

from django import template
from django.conf import settings
from django.utils import timezone
register = template.Library()

title = settings.MICROSERVICE_TITLE


@register.simple_tag
def microservice_title():
    return title


@register.filter(name='date_time')
def date(value: str):
    """ 2021-04-11T18:02:37.066850Z """
    time = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    now = datetime.now()
    difference = now - time
    if difference > timedelta(days=7):
        return time.strftime('%b %dth, %Y')
    return time.strftime('%b %dth, %Y %H:%M')
