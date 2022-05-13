from django.urls import path
from api.Cameras_Madrid.views import CamerasMadrid_APIView, CamerasMadrid_APIView_Detail
from api.Cameras_Cat.views import CamerasCat_APIView, CamerasCat_APIView_Detail
from api.Cameras_Valladolid.views import CamerasValladolid_APIView, CamerasValladolid_APIView_Detail
from api.Cameras_Zaragoza.views import CamerasZaragoza_APIView, CamerasZaragoza_APIView_Detail
from api.Cameras_Valencia.views import CamerasValencia_APIView, CamerasValencia_APIView_Detail
from api.Cameras_Malaga.views import CamerasMalaga_APIView, CamerasMalaga_APIView_Detail
from api.Cameras_Sevilla.views import CamerasSevilla_APIView, CamerasSevilla_APIView_Detail
from api.Cameras_Baleares.views import CamerasBaleares_APIView, CamerasBaleares_APIView_Detail



app_name = 'api'

urlpatterns = [
    path('v1/CamerasMadrid/', CamerasMadrid_APIView.as_view()), 
    path('v1/CamerasMadrid/<int:pk>/', CamerasMadrid_APIView_Detail.as_view()),
    path('v1/CamerasCat/', CamerasCat_APIView.as_view()),
    path('v1/CamerasCat/<int:pk>/', CamerasCat_APIView_Detail.as_view()),
    path('v1/CamerasValladolid/', CamerasValladolid_APIView.as_view()),
    path('v1/CamerasValladolid/<int:pk>/', CamerasValladolid_APIView_Detail.as_view()),
    path('v1/CamerasZaragoza/', CamerasZaragoza_APIView.as_view()),
    path('v1/CamerasZaragoza/<int:pk>/', CamerasZaragoza_APIView_Detail.as_view()),
    path('v1/CamerasValencia/', CamerasValencia_APIView.as_view()),
    path('v1/CamerasValencia/<int:pk>/', CamerasValencia_APIView_Detail.as_view()),
    path('v1/CamerasMalaga/', CamerasMalaga_APIView.as_view()),
    path('v1/CamerasMalaga/<int:pk>/', CamerasMalaga_APIView_Detail.as_view()),
    path('v1/CamerasSevilla/', CamerasSevilla_APIView.as_view()),
    path('v1/CamerasSevilla/<int:pk>/', CamerasSevilla_APIView_Detail.as_view()),
    path('v1/CamerasBaleares/', CamerasBaleares_APIView.as_view()),
    path('v1/CamerasBaleares/<int:pk>/', CamerasBaleares_APIView_Detail.as_view()),
]