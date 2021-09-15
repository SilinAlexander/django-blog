from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'actions'

router = DefaultRouter()

urlpatterns = [
    path('like-dislike/', views.LikeDislikeView.as_view(), name='like_dislike'),
    path('follow/', views.FollowView.as_view(), name='follow'),
    path('followers/', views.FollowersViewSet.as_view({'get': 'user_followers'}), name='user_followers'),
    path('following/', views.FollowersViewSet.as_view({'get': 'user_following'}), name='user_following'),
    path('followers/<user_id>/', views.FollowersViewSet.as_view({'get': 'user_followers_by_id'}),
         name='user_followers_by_id'),
    path('following/<user_id>/', views.FollowersViewSet.as_view({'get': 'user_following_by_id'}),
         name='user_following_by_id'),
    path('actions/', views.ActionListView.as_view(), name='actions'),


]

urlpatterns += router.urls
