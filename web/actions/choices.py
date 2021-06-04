from django.db.models import IntegerChoices


class LikeStatus(IntegerChoices):
    LIKE = (1, 'Like')
    DISLIKE = (-1, 'Dislike')
