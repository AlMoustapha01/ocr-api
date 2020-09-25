from rest_framework import serializers
from application.models.profilebyapplication_model import *

class ProfileByApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileByApplication
        fields = '__all__'