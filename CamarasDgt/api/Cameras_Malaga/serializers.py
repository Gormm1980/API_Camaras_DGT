from rest_framework import serializers
from .models import CamerasMalaga



class   CamerasMalagaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasMalaga
        include_fields = ('id', 'name', 'url', 'location')

