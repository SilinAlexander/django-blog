from rest_framework import serializers
from .models import LikeDislike
from blog.models import Article, Comment
from .choices import LikeObjects


class LikeDislikeSerializer(serializers.ModelSerializer):

    model = serializers.ChoiceField(choices=LikeObjects.choices)

    class Meta:
        model = LikeDislike
        fields = ('vote', 'model', 'object_id', )



