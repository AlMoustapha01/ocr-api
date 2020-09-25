from rest_framework import serializers
from user.models.entity_model import *

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

