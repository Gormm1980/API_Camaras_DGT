from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CamerasValladolidSerializers
from .models import CamerasValladolid
from rest_framework import status
from django.http import Http404
    
    
class CamerasValladolid_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        camera = CamerasValladolid.objects.all()
        serializer = CamerasValladolidSerializers(camera, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CamerasValladolidSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CamerasValladolid_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return CamerasValladolid.objects.get(pk=pk)
        except CamerasValladolid.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        camera = self.get_object(pk)
        serializer = CamerasValladolidSerializers(camera)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        camera= self.get_object(pk)
        serializer = CamerasValladolidSerializers(camera, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        camera = self.get_object(pk)
        camera.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

