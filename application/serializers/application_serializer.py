from rest_framework import serializers
from application.models.application_model import *

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

