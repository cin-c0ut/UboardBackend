from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('gyms/', views.GymList.as_view()),
    path('gyms/<int:pk>/', views.GymDetail.as_view()),
    path('climbs/', views.ClimbList.as_view()),
    path('climbs/<int:pk>/', views.ClimbDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)