from django.contrib import admin
from api.Cameras_Madrid.models import  CamerasComMadrid
from api.Cameras_Cat.models import  CamerasCat

admin.site.register(CamerasComMadrid)
admin.site.register(CamerasCat)