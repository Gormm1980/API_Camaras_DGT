from rest_framework import serializers
from .models import CamerasMadrid



class   CamerasMadridSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasMadrid
        include_fields = ('id', 'name', 'url', 'location')

