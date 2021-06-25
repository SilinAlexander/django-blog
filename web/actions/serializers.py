from typing import Union

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
        vote = self.validated_data['vote']
        if model == LikeObjects.ARTICLE:
            obj: Article = BlogService.get_article(self.validated_data['object_id'])
            print(obj)
            like_obj: LikeDislike = ActionsService.get_like_obj(obj_id=self.validated_data['object_id'], user=user,
                                                                model=obj)
            print(like_obj)
            if not like_obj:
                obj.votes.create(user=user, vote=self.validated_data['vote'])

            else:
                if vote == obj.votes:
                    like_obj.delete()
                else:
                    like_obj.vote = vote
                    like_obj.save(update_fields=['vote'])
        return self._response_data(obj)

    def _response_data(self, obj: Union[Article, Comment])->dict:
        data = {
            'like_count': obj.likes,
            'dislike_count': obj.dislikes,
        }
        return data




