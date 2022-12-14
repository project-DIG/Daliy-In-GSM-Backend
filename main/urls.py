"""
Main App URL
"""
from django.urls import path
from .views import VideoAPIView, VideoDetailView, CommentAPIView

urlpatterns = [
    path("", VideoAPIView.as_view(), name = "videoAPI"),
    path("<int:pk>",VideoDetailView.as_view(), name = "videoDetail"),
    path("<int:pk>/comment",CommentAPIView.as_view(), name = "commentAPI"),
]
