from rest_framework import serializers
from .models import CamerasSevilla



class   CamerasSevillaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasSevilla
        include_fields = ('id', 'name', 'url', 'location')

