from django.db import models

class Gym(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    #Need to add more to this model 
    #a flag for public or private to determine the get calls
    #private gyms are personal gyms that one the user has access to 