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


logger = logging.getLogger(__name__)


User = get_user_model()


class UserProfileViewSet(GenericViewSet):
    template_name ='userprofile/profile.html'

    def get_template_name(self):
        return 'userprofile/profile.html'

    def get_serializer_class(self):
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






