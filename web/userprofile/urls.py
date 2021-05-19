from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'userprofile'

router = DefaultRouter()

urlpatterns = [
    path('profile/', views.UserProfileViewSet.as_view({'get': 'profile'}), name='profile'),
    path('change-password/', views.UserProfileViewSet.as_view({'post': 'change-password'}), name='api_change_password')


]

urlpatterns += router.urls
