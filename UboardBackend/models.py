from django.db import models
from django.contrib.auth.models import User

class Gym(models.Model):
    id = models.BigAutoField()
    name = models.CharField()
    location = models.CharField()

class Wall(models.Model):
    id = models.BigAutoField()
    gym_id = models.ForeignKey(Gym, on_delete=models.CASCADE)
    name = models.CharField()
    angle = models.FloatField()
    size = models.CharField(max_length=15)
    image = models.ImageField(upload_to='walls/')

class Climb(models.Model):
    wall_id = models.ForeignKey(Wall, on_delete=models.CASCADE)
    id = models.BigAutoField()
    name = models.CharField()
    grade = models.CharField(max_length=15)
    rating = models.IntegerField()
    # climb = ml learning object??
    # key = ???

class Saved_Gym:
    id = models.BigAutoField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)

class Saved_Wall:
    id = models.BigAutoField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wall = models.ForeignKey(Wall, on_delete=models.CASCADE)

class Saved_Climb:
    id = models.BigAutoField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    climb = models.ForeignKey(Climb, on_delete=models.CASCADE)

class Climbing_Log:
    id = models.BigAutoField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    climb = models.ForeignKey(Climb, on_delete=models.CASCADE)