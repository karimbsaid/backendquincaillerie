from rest_framework import serializers
from .models import Command
from accounts.serializers import UserProfileSerializer
from productAPI.serializers import ProductListeSerializers
class CommandSerializer(serializers.ModelSerializer):
    user=UserProfileSerializer(source='user.profile',read_only=True)
    product = ProductListeSerializers(read_only=True)
    product_id=serializers.IntegerField(write_only=True)
    class Meta:
        model = Command
        fields = '__all__'
        read_only_fields = ('user', 'created_at')
