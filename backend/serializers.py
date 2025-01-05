from rest_framework import serializers
from backend.models import Gym, Wall, Profile, Climb, Climbing_Log
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

class ClimbingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climbing_Log
        fields = ['id', ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']        

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    climbs = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='climb-detail',
                                                 read_only=True)
    # saved_climbs = serializers.HyperlinkedRelatedField(many=True,
    #                                                    view_name='climb-log-detail')
    # saved_gyms = serializers.HyperlinkedRelatedField(many=True,
    #                                                  view_name='gym-detail')
    # saved_walls = serializers.HyperlinkedRelatedField(many=True,
    #                                                   view_name='wall-detail')
    
    class Meta:
        model = Profile
        fields = ['user', 'climbs']