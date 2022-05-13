from rest_framework import serializers
from .models import CamerasCoruña



class   CamerasCoruñaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasCoruña
        include_fields = ('id', 'name', 'url', 'location')

