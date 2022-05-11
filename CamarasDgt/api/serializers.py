from rest_framework import serializers
from .models import TrafficCamera, Location



class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        include_fields = ('id', 'name', 'traffic_cameras')
        
class TrafficCameraSerializers(serializers.ModelSerializer):
    class Meta:
        model = TrafficCamera
        include_fields = ('id', 'name', 'url')
       