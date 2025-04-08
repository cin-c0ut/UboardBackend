from django.db import models
from .wall import Wall
from .profile import Profile

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