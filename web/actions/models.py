from django.contrib.auth import get_user_model
from django.db import models
from .choices import LikeStatus
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


from . import managers
User = get_user_model()


class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    vote = models.IntegerField(choices=LikeStatus.choices)
    date = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    objects = models.Manager()
