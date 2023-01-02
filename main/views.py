from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import response, status
import io
from rest_framework.parsers import JSONParser
from daliyInGsm.settings import AWS_S3_CUSTOM_DOMAIN
import json
import logging


from .serializers import VideoSerializer, CommentSerializer
from .models import Video, Comment
from rest_framework import pagination


class VideoPagination(pagination.PageNumberPagination):
    page_size = 5

class VideoAPIView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = VideoPagination


    def post(self, request):
        request.data.__setitem__("video_url", f"https://{AWS_S3_CUSTOM_DOMAIN}/{request.data['video_upload']}")
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()            
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    


class VideoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



#####################################################

class CommentAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
