from rest_framework import serializers
from .models import CamerasCAM




        
class   CamerasCAMSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasCAM
        include_fields = ('id', 'name', 'url', 'location')
       