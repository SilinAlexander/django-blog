from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Follower
from .services import ActionsService
from django.template.loader import render_to_string
from userprofile.models import Profile


@receiver(post_save, sender=Follower)
def user_start_to_follow(sender, created: bool, instance: Follower, **kwargs):
    template = 'actions/start_to_follow.html'
    data = {
        'subscriber': instance.subscriber,
        'to_user': instance.to_user
    }
    action = render_to_string(template_name=template, context=data)
    print(sender, created, instance, kwargs)
    ActionsService.create_action(user=instance.subscriber, action=action, instance=instance)


@receiver(post_save, sender=Profile)
def user_change_avatar(sender, created: bool, instance: Profile, **kwargs):
    if not kwargs.get('update_fields') and 'image' not in kwargs.get('update_fields'):
        return
    template = 'actions/change_avatar.html'
    data = {
        'user': instance.user,
        'image': instance.image
    }
    print(sender, created, instance, kwargs)
    action = render_to_string(template_name=template, context=data)
    ActionsService.create_action(user=instance.user, action=action, instance=instance)


