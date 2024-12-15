from django.db import models

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
    # wall img = blob???

class Climb(models.Model):
    wall_id = models.ForeignKey(Wall, on_delete=models.CASCADE)
    id = models.BigAutoField()
    name = models.CharField()
    grade = models.CharField(max_length=15)
    rating = models.IntegerField()
    # climb = ml learning object??
    # key = ???