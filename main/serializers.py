from rest_framework.serializers import ModelSerializer
from .models import Video, Comment

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video    
        fields = ('__all__')


class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('__all__')