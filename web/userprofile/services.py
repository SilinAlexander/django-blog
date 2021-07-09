from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from . import models
from blog.choices import ArticleStatus
User = get_user_model()


class UserprofileService:

    @staticmethod
    def get_user_profile(user_id: int):
        user_likes = Count('likes')
        user_articles = Count('article_set', filter=Q(article_set__status=ArticleStatus.ACTIVE))

        return (
            User.objects
                .select_related('profile_set')
                .prefetch_related('profile_set__address_set')
                .annotate(user_likes=user_likes, user_articles=user_articles)
                .get(id=user_id)
        )

    @staticmethod
    def user_queryset():
        return User.objects.exclude(is_active=False).select_related('profile_set')
