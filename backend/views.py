from backend.models import Gym, Wall, Climb, Saved_Gym, Saved_Wall, Saved_Climb, Climbing_Log
from backend.serializers import GymSerializer, WallSerializer, Saved_GymSerializer, Saved_WallSerializer, Saved_ClimbSerializer
from rest_framework import generics

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
