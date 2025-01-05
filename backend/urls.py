from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend import views

router = DefaultRouter()
router.register(r'gyms', views.GymViewSet, basename='gym')
router.register(r'climbs', views.ClimbViewSet, basename='climbs')
router.register(r'profiles', views.ProfileViewSet, basename='profiles')

urlpatterns = [
    path('', include(router.urls)),
]