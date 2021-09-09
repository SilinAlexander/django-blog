from django.contrib import admin
from .models import LikeDislike, Follower, Action
from django.contrib.contenttypes.admin import GenericTabularInline


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_select_related = ('user', 'content_type')
    list_display = ('user', 'content_type', 'vote', 'date', 'content_object')
    list_filter = ('vote',)


class LikeDislikeInline(GenericTabularInline):
    model = LikeDislike
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('to_user', 'subscriber', )
    date_hierarchy = 'date'


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'action')
    date_hierarchy = 'date'
