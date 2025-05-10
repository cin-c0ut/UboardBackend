from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from backend.models import Wall
from backend.serializers import WallSerializer

class WallViewSet(viewsets.ModelViewSet):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer
    
    @action(detail=False)
    def filter_gym(self, request):
        gym_pk = request.query_params.get('gym_id')
        queryset = Wall.objects.filter(gym_id=gym_pk)
        serializer = WallSerializer(queryset,
                                many=True,
                                context={'request': request}) #should return a list of wallls
                                                              #if empty we handle this on frontend we should still return an empty set. 
        return Response(serializer.data) 