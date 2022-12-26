"""
Main App URL
"""
from django.urls import path
from .views import VideoAPIView ##VideoDetailView

urlpatterns = [
    path("", VideoAPIView.as_view(), name = "videoAPI"),
    ## path("<int:pk>",VideoDetailView.as_view(), name = "videoDetail")
]
