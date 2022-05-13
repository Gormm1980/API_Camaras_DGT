from rest_framework import serializers
from .models import CamerasComMadrid



class   CamerasComMadridSerializers(serializers.ModelSerializer):
    class Meta:
        model = CamerasComMadrid
        include_fields = ('id', 'name', 'url', 'location')

