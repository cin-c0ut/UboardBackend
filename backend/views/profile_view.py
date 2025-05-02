from rest_framework import viewsets, status
from rest_framework.response import Response
from backend.models import Profile
from backend.serializers import ProfileSerializer
from backend.permissions import IsOwnerOrReadOnly

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        is_user_profile = self.request.user == self.get_object().user
        context.update({'is_user_profile': is_user_profile})     
        return context

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user

        self.perform_destroy(instance)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)