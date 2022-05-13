from rest_framework import serializers
from .models import CamerasZaragoza



class   CamerasZaragozaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasZaragoza
        include_fields = ('id', 'name', 'url', 'location')

