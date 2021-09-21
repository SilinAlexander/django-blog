from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from main.pagination import DefaultPagination

from actions.serializers import ActionListSerializer
from actions.services import ActionsService

User = get_user_model()


class TemplateAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    template_name = ''

    @method_decorator(name='create', decorator=swagger_auto_schema(auto_schema=None))
    def get(self, request, *args, **kwargs):
        return Response()


class IndexView(ListModelMixin, TemplateAPIView):
    serializer_class = ActionListSerializer
    pagination_class = DefaultPagination

    @property
    def template_name(self):
        if self.request.user.is_authenticated:
            return 'actions/index.html'
        return 'index.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return ActionsService.get_following_action(self.request.user)


