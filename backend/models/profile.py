from django.db import models
from django.contrib.auth.models import User
from .wall import Wall
from .gym import Gym
from .climb import Climb

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    saved_walls = models.ManyToManyField(Wall, blank=True)
    saved_climbs = models.ManyToManyField(Climb, related_name='profile_saved', blank=True)
    logged_climbs = models.ManyToManyField(Climb, related_name='profile_logged',
                                          through='Climbing_Log',
                                          blank=True)
    saved_gyms = models.ManyToManyField(Gym, blank=True) 