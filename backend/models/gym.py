from django.db import models

class Gym(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    @classmethod
    def create_gym(cls, name, location):
        """
        Class method to create a new gym
        Usage: gym = Gym.create_gym(name="Climb Central", location="Singapore")
        """
        return cls.objects.create(name=name, location=location)

    def add_wall(self, name, angle, size, image):
        """
        Instance method to add a wall to this gym
        Usage: gym.add_wall(name="Main Wall", angle=15, size="Large", image=wall_image)
        """
        from .wall import Wall  # Import here to avoid circular imports
        return Wall.objects.create(
            gym_id=self,
            name=name,
            angle=angle,
            size=size,
            image=image
        )

    def get_walls(self):
        """
        Instance method to get all walls in this gym
        Usage: walls = gym.get_walls()
        """
        return self.wall_set.all()  # Django automatically creates this reverse relation

    def __str__(self):
        """
        String representation of the model
        Usage: print(gym) or str(gym)
        """
        return f"{self.name} - {self.location}" 