from rest_framework import serializers
from actions.choices import LikeIconStatus, LikeStatus
from main.serializers import UserSerializer
from .models import Category, Article, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'author', 'content', 'updated', 'article')


class CategorySerializer(serializers.ModelSerializer):

    slug = serializers.SlugField(read_only=True, allow_unicode=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url')
    author = UserSerializer()
    category = CategorySerializer()
    comments_count = serializers.IntegerField()
    like_status = serializers.SerializerMethodField(method_name='get_like_status')

    def get_like_status(self, obj) -> str:
        user = self.context['request'].user
        if not user.is_authenticated:
            return LikeIconStatus.CANCELED
        if like_obj := obj.votes.filter(user=user).first():
            return LikeIconStatus.LIKED if like_obj.vote == LikeStatus.LIKE else LikeIconStatus.DISLIKED
        return LikeIconStatus.CANCELED

    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'author', 'category', 'created',
                  'updated', 'comments_count', 'image', 'content', 'likes', 'dislikes', 'like_status')


class FullArticleSerializer(ArticleSerializer):

    comments = CommentSerializer(source='comment_set', many=True)

    class Meta(ArticleSerializer.Meta):
        fields = ArticleSerializer.Meta.fields + ('content', 'comments',)
