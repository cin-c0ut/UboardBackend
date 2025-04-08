from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import GymViewSet, WallViewSet, ClimbViewSet, ProfileViewSet, ClimbingLogViewSet

router = DefaultRouter()
router.register(r'gyms', GymViewSet, basename='gym')
router.register(r'walls', WallViewSet, basename='wall')
router.register(r'climbs', ClimbViewSet, basename='climb')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'climbing_logs', ClimbingLogViewSet, basename='climbing_log')

urlpatterns = [
    path('', include(router.urls)),
]