from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('phone', 'image')


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source='profile_set')

    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'is_active', 'profile')


