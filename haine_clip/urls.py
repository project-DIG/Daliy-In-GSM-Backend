from django.urls import path,include
from rest_framework import routers
from .views import UserListViewSet

router = routers.DefaultRouter()
router.register('info', UserListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]