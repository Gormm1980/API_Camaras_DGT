from django.urls import path
from api.Cameras_Madrid.views import CamerasComMadrid_APIView, CamerasComMadrid_APIView_Detail
from api.Cameras_Cat.views import CamerasCat_APIView, CamerasCat_APIView_Detail



app_name = 'api'

urlpatterns = [
    path('v1/CamerasComMadrid/', CamerasComMadrid_APIView.as_view()), 
    path('v1/CamerasComMadrid/<int:pk>/', CamerasComMadrid_APIView_Detail.as_view()),
    path('v1/CamerasCat/', CamerasCat_APIView.as_view()),
    path('v1/CamerasCat/<int:pk>/', CamerasCat_APIView_Detail.as_view()),
    
 
    
]