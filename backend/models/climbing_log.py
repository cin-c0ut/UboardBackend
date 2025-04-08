from django.db import models
from django.utils import timezone
from .profile import Profile
from .climb import Climb

class Climbing_Log(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    climb = models.ForeignKey(Climb, on_delete=models.CASCADE)
    date_logged = models.DateTimeField(default=timezone.now) 