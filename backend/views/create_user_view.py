from backend.serializers import CreateUserProfileSerializer
from rest_framework import mixins, viewsets
from django.conf import settings

class CreateUserViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = settings.AUTH_USER_MODEL.objects.all()
    serializer_class = CreateUserProfileSerializer