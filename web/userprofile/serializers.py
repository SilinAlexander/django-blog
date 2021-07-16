from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Address
from dj_rest_auth.serializers import PasswordChangeSerializer

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
        fields = ('id', 'email', 'full_name', 'is_active', 'profile', 'user_likes', 'user_posts')


class ChangePasswordSerializer(PasswordChangeSerializer):
    pass


class ChangeAvatarSerializer(serializers.ModelSerializer):

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

    class Meta:
        model = User
        fields = ('id', 'full_name', 'image')
