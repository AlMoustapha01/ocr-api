from rest_framework import serializers
from invoice.models.file_model import *

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"