from django.urls import path
from .views import TrafficCamera_APIView, Location_APIView, TrafficCamera_APIView_Detail, Location_APIView_Detail

app_name = 'api'

urlpatterns = [
    path('v1/TrafficCamera/', TrafficCamera_APIView.as_view()), 
    path('v1/TrafficCamera/<int:pk>/', TrafficCamera_APIView_Detail.as_view()),
    path('v1/Location/', Location_APIView.as_view()),
    path('v1/Location/<int:pk>/', Location_APIView_Detail.as_view()),
    
]