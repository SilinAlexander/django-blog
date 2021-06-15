import logging

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from . import services
from . import serializers
from rest_framework.parsers import JSONParser, MultiPartParser


logger = logging.getLogger(__name__)


User = get_user_model()


class UserProfileViewSet(GenericViewSet):
    template_name = 'userprofile/profile.html'
    # parser_classes = (MultiPartParser, JSONParser)

    def get_template_name(self):
        return 'userprofile/profile.html'

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
        obj = get_object_or_404(self.get_queryset(), id=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

    def profile(self, request):
        serializer = self.get_serializer(instance=self.get_object())
        return Response(serializer.data)

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
