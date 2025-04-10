from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from backend.models import Climb, Profile
from backend.serializers import ClimbSerializer
from backend.permissions import IsOwnerOrReadOnly

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