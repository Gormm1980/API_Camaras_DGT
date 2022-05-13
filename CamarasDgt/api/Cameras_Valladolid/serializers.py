from rest_framework import serializers
from .models import CamerasValladolid



class   CamerasValladolidSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasValladolid
        include_fields = ('id', 'name', 'url', 'location')

