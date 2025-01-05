from backend.models import Gym, Wall, Climb, Saved_Gym, Saved_Wall, Saved_Climb, Climbing_Log
from django.contrib.auth.models import User
from backend.serializers import GymSerializer, WallSerializer, ClimbSerializer, Saved_GymSerializer, Saved_WallSerializer, Saved_ClimbSerializer, UserSerializer
from backend.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'gyms': reverse('gym-list', request=request, format=format)
    })

class GymList(generics.ListCreateAPIView):
    """
    List all gyms, or create a new gym
    """
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    
class GymDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete gym.
    """
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class ClimbList(generics.ListCreateAPIView):
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ClimbDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer