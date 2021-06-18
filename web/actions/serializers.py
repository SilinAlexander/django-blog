from rest_framework import serializers
from .models import LikeDislike
from blog.models import Article, Comment
from .choices import LikeObjects, LikeStatus


class LikeDislikeSerializer(serializers.Serializer):

    model = serializers.ChoiceField(choices=LikeObjects.choices)
    vote = serializers.ChoiceField(choices=LikeStatus.choices)
    object_id = serializers.IntegerField(min_value=1)

    def save(self, **kwargs):
        print(self.validated_data)



