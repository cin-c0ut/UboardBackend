from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend import views

router = DefaultRouter()
router.register(r'gyms', views.GymViewSet, basename='gym')
router.register(r'walls', views.WallViewSet, basename='wall')
router.register(r'climbs', views.ClimbViewSet, basename='climb')
router.register(r'profiles', views.ProfileViewSet, basename='profile')
router.register(r'climbing_logs', views.ClimbingLogViewSet, basename='climbing_log')

urlpatterns = [
    path('', include(router.urls)),
]