from django.conf import settings
from .models import LikeDislike
from main.decorators import except_shell
from django.contrib.contenttypes.models import ContentType


class ActionsService:
    @staticmethod
    @except_shell((LikeDislike.DoesNotExist, ))
    def get_like_obj(obj_id: int, user, model):
        content_type = ContentType.objects.get_for_model(model)
        print(content_type)
        return LikeDislike.objects.get(object_id=obj_id, user=user, content_type=content_type)

    @staticmethod
    def is_user_followed(user, to_user_id: int) -> bool:
        return user.following.filter(to_user_id=to_user_id).exists()

    @staticmethod
    def follow_user(user, to_user_id: int):
        return user.following.create(to_user_id=to_user_id)

    @staticmethod
    def unfollow_user(user, to_user_id: int):
        return user.following.filter(to_user_id=to_user_id).delete()
