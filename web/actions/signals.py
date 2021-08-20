from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Follower
from .services import ActionsService


@receiver(post_save, sender=Follower)
def user_start_to_follow(sender, created: bool, instance: Follower, **kwargs):
    action = f'user { instance.subscriber } started to follow { instance.to_user } '
    print(sender, created, instance, kwargs)
    ActionsService.create_action(user=instance.subscriber, action=action, instance=instance)


