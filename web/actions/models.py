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


class Follower(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_from')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_to')
    date = models.DateTimeField(auto_now=True, db_index=True)
    objects = models.Manager()

    class Meta:
        unique_together = ('subscriber', 'to_user')
        ordering = ('-date', )
