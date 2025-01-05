from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Gym(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class Wall(models.Model):
    id = models.BigAutoField(primary_key=True)
    gym_id = models.ForeignKey(Gym, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    angle = models.FloatField()
    size = models.CharField(max_length=15)
    image = models.ImageField(upload_to='walls/')
    boxes = models.JSONField() 
    confidences = models.JSONField()
    classes = models.JSONField()
    masks = models.JSONField(null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    saved_walls = models.ManyToManyField(Wall, blank=True)
    saved_climbs = models.ManyToManyField('Climb', related_name='profile_saved', blank=True)
    logged_climbs = models.ManyToManyField('Climb', related_name='profile_logged',
                                          through='Climbing_Log',
                                          blank=True)
    saved_gyms = models.ManyToManyField(Gym, blank=True)

class Climb(models.Model):
    wall_id = models.ForeignKey(Wall, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, related_name='climbs', on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=15)
    rating = models.IntegerField()
    holds = models.JSONField() # Will hold array of ints corresponding to which holds will be used
                               # each int corresponds to a bounding box in Wall class
    # Not sure how to integrate how what each hold is (foot only, hand only, start, end)
        # maybe do separate class??

class Climbing_Log(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    climb = models.ForeignKey(Climb, on_delete=models.CASCADE)
    date_logged = models.DateTimeField(default=timezone.now)