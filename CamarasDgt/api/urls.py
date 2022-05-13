from django.urls import path
from .views import CamerasCAM_APIView, CamerasCAM_APIView_Detail

app_name = 'api'

urlpatterns = [
    path('v1/CamerasCAM/', CamerasCAM_APIView.as_view()), 
    path('v1/CamerasCAM/<int:pk>/', CamerasCAM_APIView_Detail.as_view()),
 
    
]