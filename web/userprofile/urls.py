from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'userprofile'

router = DefaultRouter()

urlpatterns = [
    path('profile/', views.UserProfileViewSet.as_view({'get': 'profile'}))

]

urlpatterns += router.urls
