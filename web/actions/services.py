from django.conf import settings
from django.contrib.auth import get_user_model

from .models import LikeDislike, Follower, Action
from main.decorators import except_shell
from django.contrib.contenttypes.models import ContentType


User = get_user_model()


class ActionsService:
    @staticmethod
    @except_shell((LikeDislike.DoesNotExist, ))
    def get_like_obj(obj_id: int, user, model):
        content_type = ContentType.objects.get_for_model(model)
        print(content_type)
        return LikeDislike.objects.get(object_id=obj_id, user=user, content_type=content_type)

    @staticmethod
    def is_user_followed(user, to_user_id: int) -> bool:
        return Follower.objects.filter(subscriber=user, to_user_id=to_user_id).exists()

    @staticmethod
    def follow_user(user, to_user_id: int):
        return Follower.objects.create(subscriber=user, to_user_id=to_user_id)

    @staticmethod
    def unfollow_user(user, to_user_id: int):
        return Follower.objects.filter(subscriber=user, to_user_id=to_user_id).delete()

    @staticmethod
    def get_followers_list(user):
        return user.followers.all()

    @staticmethod
    def get_following_list(user):
        return user.following.all()

    @staticmethod
    def create_action(user, action: str, instance):
        return Action.objects.create(user=user, action=action, content_object=instance)

    @staticmethod
    @except_shell(User.DoesNotExist, )
    def get_user(user_id):
        return User.objects.get(id=user_id)

    @staticmethod
    def get_following_action(user):
        following = ActionsService.get_following_list(user)
        return Action.objects.filter(user__in=following)
