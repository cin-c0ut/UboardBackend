from rest_framework import viewsets
from backend.models import Gym
from backend.serializers import GymSerializer

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer 