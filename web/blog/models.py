from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from rest_framework.reverse import reverse_lazy
from django.contrib.contenttypes.fields import GenericRelation

from actions.choices import LikeStatus
from actions.models import LikeDislike

from . import managers
from .choices import ArticleStatus

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def save(self, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='article_set')
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)
    content = models.TextField(db_index=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article_set')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(choices=ArticleStatus.choices, default=ArticleStatus.INACTIVE)
    image = models.ImageField(upload_to='articles/', blank=True, default='no-image-available.jpg')
    votes = GenericRelation(LikeDislike, related_query_name='articles')
    objects = models.Manager()

    @property
    def short_title(self):
        return self.title[:30]

    def __str__(self):
        return '{title} - {author}'.format(title=self.short_title, author=self.author)

    def save(self, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(**kwargs)

    def get_absolute_url(self):
        url = 'blog:post-detail'
        return reverse_lazy(url, kwargs={'slug': self.slug})

    @property
    def likes(self) -> int:
        return self.votes.filter(vote=LikeStatus.LIKE).count()

    @property
    def dislikes(self) -> int:
        return self.votes.filter(vote=LikeStatus.DISLIKE).count()

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ('-updated', '-created', 'id')


class Comment(models.Model):
    author = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment_set', blank=True)
    content = models.TextField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_set')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    votes = GenericRelation(LikeDislike, related_query_name='comments')

    objects = models.Manager()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    @property
    def likes(self) -> int:
        return self.votes.filter(vote=LikeStatus.LIKE).count()

    @property
    def dislikes(self) -> int:
        return 0
