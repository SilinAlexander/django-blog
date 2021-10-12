from django.dispatch import receiver
from django.db.models.signals import post_save
from .services import UserprofileService
from .models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, created: bool, instance: User, **kwargs):
    print(sender, created, instance, kwargs)
    if created:
        Profile.objects.create(user=instance)
