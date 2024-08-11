# accounts/serializers.py

from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    username =serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ['username','postalCart', 'city', 'phone_number']
    def get_username(self, obj):
        return obj.user.username
