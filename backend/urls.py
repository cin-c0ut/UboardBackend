from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('', views.api_root),
    path('gyms/',
         views.GymList.as_view(),
         name='gym-list'),
    path('gyms/<int:pk>/',
         views.GymDetail.as_view(),
         name='gym-detail'),
    path('climbs/',
         views.ClimbList.as_view(),
         name='climb-list'),
    path('climbs/<int:pk>/',
         views.ClimbDetail.as_view(),
         name='climb-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)