from rest_framework.serializers import ModelSerializer
from .models import Video

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video    
        fields = ('id','title', 'video_url', 'like', 'dislike', 'tag', 'uploader')
        read_only_fields = ()