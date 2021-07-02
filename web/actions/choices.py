from django.db.models import IntegerChoices, TextChoices


class LikeStatus(IntegerChoices):
    LIKE = (1, 'Like')
    DISLIKE = (-1, 'Dislike')


class LikeObjects(TextChoices):
    ARTICLE = ('article', 'Article')
    COMMENT = ('comment', 'Comment')


class LikeIconStatus(TextChoices):
    LIKED = ('liked', 'Liked')
    DISLIKED = ('disliked', 'Disliked')
    CANCELED = ('canceled', 'Canceled')
