from backend.models import Gym, Wall, Climb, Profile, Climbing_Log
from django.contrib.auth.models import User
from backend.serializers import GymSerializer, WallSerializer, ClimbSerializer, ProfileSerializer, ClimbingLogSerializer
from backend.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class WallViewSet(viewsets.ModelViewSet):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer

class ClimbViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides 'list' and 'CRUD' actions.
    """
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ClimbingLogViewSet(viewsets.ModelViewSet):
    queryset = Climbing_Log.objects.all()
    serializer_class = ClimbingLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)