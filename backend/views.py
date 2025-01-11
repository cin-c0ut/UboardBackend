from backend.models import Gym, Wall, Climb, Profile, Climbing_Log
from django.contrib.auth.models import User
from backend.serializers import GymSerializer, WallSerializer, ClimbSerializer, ProfileSerializer, ClimbingLogSerializer
from backend.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class WallViewSet(viewsets.ModelViewSet):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer
    
    @action(detail=False)
    def filter_gym(self, request):
        gym_pk = request.query_params.get('gym_id')
        queryset = Wall.objects.filter(gym_id=gym_pk)
        if queryset.exists():
            serializer = WallSerializer(queryset,
                                        many=True,
                                        context={'request': request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ClimbViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides 'list' and 'CRUD' actions.
    """
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        currUser = Profile.objects.get(user=self.request.user.id)
        serializer.save(user_id=currUser)

    @action(detail=False)
    def filter_wall(self, request):
        wall_pk = request.query_params.get('wall_id')
        queryset = Climb.objects.all().filter(wall_id=wall_pk)
        if queryset.exists():
            serializer = ClimbSerializer(queryset,
                                         many=True,
                                         context={'request': request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

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

    @action(detail=False)
    def filter_user(self, request):
        profile_pk = request.query_params.get('profile_id')
        if profile_pk:
            queryset = Climbing_Log.objects.filter(profile=profile_pk)
        else:
            queryset = Climbing_Log.objects.filter(profile=request.user.id)
        if queryset.exists():
            serializer = ClimbingLogSerializer(queryset,
                                               many=True,
                                               context={'request': request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)