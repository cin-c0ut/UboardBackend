from rest_framework import serializers
from backend.models import Gym, Wall, Climb, Saved_Gym, Saved_Wall, Saved_Climb, Climbing_Log
from django.contrib.auth.models import User

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'

class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = '__all__'

class ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climb
        fields = '__all__'
    
    user_id = serializers.ReadOnlyField(source='user_id.username')

class Saved_GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved_Gym
        fields = '__all__'

class Saved_WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved_Wall
        fields = '__all__'

class Saved_ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved_Climb
        fields = '__all__'

class Climbing_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climbing_Log
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    climbs = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='climb-detail',
                                                 read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'climbs']