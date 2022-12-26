from rest_framework.generics import ListCreateAPIView
from rest_framework import response, status, permissions

from .serializers import VideoSerializer
from .models import Video

class VideoAPIView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

