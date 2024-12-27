from django.db import models
from django.contrib.auth.models import User

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


class Climb(models.Model):
    wall_id = models.ForeignKey(Wall, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='climbs', on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=15)
    rating = models.IntegerField()
    holds = models.JSONField() # Will hold array of ints corresponding to which holds will be used
                               # each int corresponds to a bounding box in Wall class
    # Not sure how to integrate how what each hold is (foot only, hand only, start, end)
        # maybe do separate class??

class Saved_Gym:
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)

class Saved_Wall:
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wall = models.ForeignKey(Wall, on_delete=models.CASCADE)

class Saved_Climb:
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    climb = models.ForeignKey(Climb, on_delete=models.CASCADE)

class Climbing_Log:
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    climb = models.ForeignKey(Climb, on_delete=models.CASCADE)