from rest_framework import serializers
from .models import CamerasValencia



class   CamerasValenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasValencia
        include_fields = ('id', 'name', 'url', 'location')

