from rest_framework import serializers
from backend.models import Gym, Wall, Climb, Saved_Gym, Saved_Wall, Saved_Climb

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        field = '__all__'

class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        field = '__all__'

class ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climb
        field = '__all__'

class Saved_Gym(serializers.ModelSerializer):
    class Meta:
        model = Saved_Gym
        field = '__all__'

class Saved_Wall(serializers.ModelSerializer):
    class Meta:
        model = Saved_Wall
        field = '__all__'

class Saved_Climb(serializers.ModelSerializer):
    class Meta:
        model = Saved_Climb
        field = '__all__'

class Climbing_Log(serializers.ModelSerializer):
    class Meta:
        field = '__all__'