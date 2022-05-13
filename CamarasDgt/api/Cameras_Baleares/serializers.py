from rest_framework import serializers
from .models import CamerasBaleares



class   CamerasBalearesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasBaleares
        include_fields = ('id', 'name', 'url', 'location')

