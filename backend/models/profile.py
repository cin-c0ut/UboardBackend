from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    saved_walls = models.ManyToManyField('Wall', blank=True)
    saved_climbs = models.ManyToManyField('Climb', related_name='profile_saved', blank=True)
    logged_climbs = models.ManyToManyField('Climb', related_name='profile_logged',
                                          through='Climbing_Log',
                                          blank=True)
    saved_gyms = models.ManyToManyField('Gym', blank=True) 