from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('gyms/', views.GymList.as_view()),
    path('gyms/<int:pk>/', views.GymDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)