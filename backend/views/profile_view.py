from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from backend.models import Profile
from backend.serializers import ProfileSerializer

class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user

        self.perform_destroy(instance)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)