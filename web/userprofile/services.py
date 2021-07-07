from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Count
from . import models
User = get_user_model()


class UserprofileService:

    @staticmethod
    def get_user_profile(user_id: int):
        return (
            User.objects
                .select_related('profile_set')
                .prefetch_related('profile_set__address_set')
                .get(id=user_id)
        )

