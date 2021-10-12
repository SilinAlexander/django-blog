from typing import Union

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import LikeDislike, Action
from blog.models import Article, Comment
from .choices import LikeObjects, LikeStatus, LikeIconStatus, SubscribeStatus
from blog.services import BlogService
from .services import ActionsService

User = get_user_model()


class LikeDislikeSerializer(serializers.Serializer):
    model = serializers.ChoiceField(choices=LikeObjects.choices)
    vote = serializers.ChoiceField(choices=LikeStatus.choices)
    object_id = serializers.IntegerField(min_value=1)

    def save(self, **kwargs):
        print(self.validated_data)
        model = self.validated_data['model']
        user = self.context['request'].user
        vote = self.validated_data['vote']
        icon_status = LikeIconStatus.LIKED if vote == LikeStatus.LIKE else LikeIconStatus.DISLIKED
        if model == LikeObjects.ARTICLE:
            obj: Article = BlogService.get_article(self.validated_data['object_id'])
            print(obj)
        else:
            obj: Comment = BlogService.get_comment(self.validated_data['object_id'])
        like_obj: LikeDislike = ActionsService.get_like_obj(
            obj_id=self.validated_data['object_id'], user=user, model=obj)
        print(like_obj)
        if not like_obj:
            obj.votes.create(user=user, vote=self.validated_data['vote'])

        else:
            if vote == like_obj.vote:
                like_obj.delete()
                icon_status = LikeIconStatus.CANCELED
            else:
                like_obj.vote = vote
                like_obj.save(update_fields=['vote'])
        print(icon_status)
        return self._response_data(obj, icon_status)

    def _response_data(self, obj: Union[Article, Comment], icon_status: str) -> dict:
        data = {
            'like_count': obj.likes,
            'dislike_count': obj.dislikes,
            'status': icon_status,
        }
        return data


class SubscriberToUserSerializer(serializers.Serializer):

    to_user = serializers.IntegerField(min_value=1)

    def save(self, **kwargs):
        user = self.context['request'].user
        print(user)
        if not ActionsService.is_user_followed(user, self.validated_data['to_user']):
            ActionsService.follow_user(user, self.validated_data['to_user'])
            subscribe_status = SubscribeStatus.UNFOLLOW
        else:
            ActionsService.unfollow_user(user, self.validated_data['to_user'])
            subscribe_status = SubscribeStatus.FOLLOW
        return self._response_data(subscribe_status)

    def validate_to_user(self, to_user: int):
        if self.context['request'].user.id == to_user:
            raise serializers.ValidationError('You can not subscribe by yourself')
        return to_user

    def _response_data(self, subscribe_status: str):
        data = {
            'status': subscribe_status
        }
        return data


class UserFollowersSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='profile_set.image')
    profile_url = serializers.URLField(source='get_absolute_url')
    follow = serializers.SerializerMethodField(method_name='get_follow')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'image', 'profile_url', 'follow')

    def get_follow(self, obj):
        user = self.context['request'].user
        if user == obj:
            return None
        if not ActionsService.is_user_followed(user, obj.id):
            subscribe_status = SubscribeStatus.FOLLOW
        else:
            subscribe_status = SubscribeStatus.UNFOLLOW
        return subscribe_status


class ActionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ('user', 'date', 'action')
