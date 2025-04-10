from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from backend.views import GymViewSet, WallViewSet, ClimbViewSet, ProfileViewSet, ClimbingLogViewSet, CreateUserViewSet

router = DefaultRouter()
router.register(r'gyms', GymViewSet, basename='gym')
router.register(r'walls', WallViewSet, basename='wall')
router.register(r'climbs', ClimbViewSet, basename='climb')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'climbing_logs', ClimbingLogViewSet, basename='climbing_log')
router.register(r'register', CreateUserViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Uboard API",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]