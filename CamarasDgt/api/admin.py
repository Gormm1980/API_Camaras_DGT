from django.contrib import admin
from api.Cameras_Madrid.models import  CamerasMadrid
from api.Cameras_Cat.models import  CamerasCat
from api.Cameras_Valladolid import CamerasValladolid
from api.Cameras_Zaragoza.models import  CamerasZaragoza
from api.Cameras_Valencia.models import CamerasValencia
from.api.Cameras_Malaga.models import CamerasMalaga
from api.Cameras_Coruña.models import CamerasCoruña
from.api.Camaras_Sevilla.models import CamerasSevilla
from.api.Camaras_Baleares.models import CamerasBaleares

admin.site.register(CamerasMadrid)
admin.site.register(CamerasCat)
admin.site.register(CamerasValladolid)
admin.site.register(CamerasZaragoza)
admin.site.register(CamerasValencia)
admin.site.register(CamerasMalaga)
admin.site.register(CamerasCoruña)
admin.site.register(CamerasSevilla)
admin.site.register(CamerasBaleares)