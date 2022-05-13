from rest_framework import serializers
from .models import CamerasComMadrid, CamerasCat



class   CamerasCatSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasCat
        include_fields = ('id', 'name', 'url', 'location')
             