from rest_framework import serializers
from .models import LikeDislike
from blog.models import Article, Comment
from .choices import LikeObjects, LikeStatus
from blog.services import BlogService
from .services import ActionsService


class LikeDislikeSerializer(serializers.Serializer):

    model = serializers.ChoiceField(choices=LikeObjects.choices)
    vote = serializers.ChoiceField(choices=LikeStatus.choices)
    object_id = serializers.IntegerField(min_value=1)

    def save(self, **kwargs):
        print(self.validated_data)
        model = self.validated_data['model']
        user = self.context['request'].user
        if model == LikeObjects.ARTICLE:
            obj = BlogService.get_article(self.validated_data['object_id'])
            print(obj)
            like_obj = ActionsService.get_like_obj(obj_id=self.validated_data['object_id'], user=user, model=obj)
            print(like_obj)
            if not like_obj:
                obj.votes.create(user=user, vote=self.validated_data['vote'])





