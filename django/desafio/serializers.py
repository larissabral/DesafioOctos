from .models import Camera
from rest_framework import serializers


# Serializers define the API representation.
class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'nome', 'serie', 'fabricante']
