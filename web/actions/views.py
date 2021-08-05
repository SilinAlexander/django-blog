import logging
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from .services import ActionsService
from . import services
from . import serializers

logger = logging.getLogger(__name__)


class LikeDislikeView(GenericAPIView):

    serializer_class = serializers.LikeDislikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data)


class FollowView(CreateAPIView):

    serializer_class = serializers.SubscriberToUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class FollowersViewSet(GenericViewSet, ListModelMixin):

    serializer_class = serializers.UserFollowersSerializer

    def get_queryset(self):
        if self.action == 'user_followers':
            return ActionsService.get_followers_list
        if self.action == 'user_following':
            return ActionsService.get_following_list

    def user_followers(self, request):
        return self.list(request)

    def user_following(self, request):
        return self.list(request)
