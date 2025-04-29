from backend.serializers import CreateUserProfileSerializer
from rest_framework import mixins, viewsets
from django.contrib.auth.models import User

class CreateUserViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserProfileSerializer