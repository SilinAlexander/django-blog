from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'userprofile'

router = DefaultRouter()

urlpatterns = [
    path('profile/', views.UserProfileViewSet.as_view({'get': 'profile', 'put': 'update'}), name='profile'),
    path('profile/change-password/', views.UserProfileViewSet.as_view({'post': 'change_password'}),
         name='api_change_password'),
    path('profile/change-avatar/', views.UserProfileViewSet.as_view({'post': 'change_avatar'}),
         name='api_change_avatar'),
    path('users/', views.UserProfileViewSet.as_view({'get': 'get_user_list'}), name='user_list'),
    path('profile/id/<user_id>/', views.UserProfileViewSet.as_view({'get': 'user_detail_by_id'}), name='user_by_id'),



]

urlpatterns += router.urls
