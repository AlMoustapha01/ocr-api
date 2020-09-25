from rest_framework import serializers
from user.models.user_model import *
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UsersSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Users
        fields = '__all__'