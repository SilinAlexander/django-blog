import logging

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from .services import UserprofileService
from . import serializers
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser, MultiPartParser


logger = logging.getLogger(__name__)


User = get_user_model()


class UserProfileViewSet(GenericViewSet):
    template_name = 'userprofile/profile.html'
    # parser_classes = (MultiPartParser, JSONParser)

    def get_template_name(self):
        if self.action == 'profile':
            return 'userprofile/profile.html'
        elif self.action == 'user_detail_by_id':
            return 'userprofile/profile_by_id.html'

    def get_serializer_class(self):
        if self.action == 'change_password':
            return serializers.ChangePasswordSerializer
        if self.action == 'change_avatar':
            return serializers.ChangeAvatarSerializer
        if self.action == 'update':
            return serializers.UpdateProfileSerializer
        return serializers.UserProfileSerializer

    def get_queryset(self):

        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = UserprofileService.get_user_profile(user_id=self.request.user.id)
        self.check_object_permissions(self.request, obj)

        return obj

    def profile(self, request):
        serializer = self.get_serializer(instance=self.get_object())
        return Response(serializer.data, template_name=self.get_template_name())

    def change_password(self, request):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'New password has been saved'})

    def change_avatar(self, request):
        profile = request.user.profile_set
        serializer = self.get_serializer(instance=profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request):
        serializer = self.get_serializer(instance=request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def user_detail_by_id(self, request, user_id):

        user = UserprofileService.get_user_profile(user_id=user_id)
        serializer = self.get_serializer(instance=user)
        return Response(serializer.data, template_name=self.get_template_name())


class UserListView(GenericAPIView):

    template_name = 'userprofile/users.html'

    serializer_class = UserSerializer

    def get_queryset(self):
        return UserprofileService.user_queryset()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            'users': serializer.data
        }
        return Response(data, template_name=self.template_name)
