from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Address
from dj_rest_auth.serializers import PasswordChangeSerializer
from actions.services import ActionsService
from actions.choices import SubscribeStatus

User = get_user_model()


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'region', 'city', 'street', 'index')


class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer(source='address_set', many=True)

    class Meta:
        model = Profile
        fields = ('phone', 'image', 'address')


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source='profile_set')

    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'is_active', 'profile', 'user_likes', 'user_posts', 'followers_count',
                  'following_count')


class ChangePasswordSerializer(PasswordChangeSerializer):
    pass


class ChangeAvatarSerializer(serializers.ModelSerializer):

    def save(self):
        image = self.validated_data.get('image')
        self.instance.image = image
        self.instance.save(update_fields=['image'])

    class Meta:
        model = Profile
        fields = ('image', )


class UpdateProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=2)
    last_name = serializers.CharField(min_length=2)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender', 'birthday')


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='profile_set.image')
    subscribe = serializers.SerializerMethodField(method_name='get_subscribe_status')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'image', 'subscribe')

    def get_subscribe_status(self, user):
        subscriber = self.context['request'].user
        if not subscriber.is_authenticated:
            return None
        if ActionsService.is_user_followed(subscriber, user.id):
            return SubscribeStatus.UNFOLLOW
        return SubscribeStatus.FOLLOW
