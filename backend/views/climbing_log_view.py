from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from backend.models import Climbing_Log
from backend.serializers import ClimbingLogSerializer
from backend.permissions import IsOwnerOrReadOnly

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