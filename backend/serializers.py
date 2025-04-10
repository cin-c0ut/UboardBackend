from rest_framework import serializers
from backend.models import Gym, Wall, Profile, Climb, Climbing_Log
from django.contrib.auth.models import User

class GymSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Gym
        fields = '__all__'

class WallSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Wall
        fields = '__all__'

class ClimbSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.HyperlinkedRelatedField(read_only=True,
                                               view_name='profile-detail')

    class Meta:
        model = Climb
        fields = '__all__'

class ClimbingLogSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    profile = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(),
                                                  view_name='profile-detail')
    climb = serializers.HyperlinkedRelatedField(queryset=Climb.objects.all(),
                                                view_name='climb-detail')
    
    class Meta:
        model = Climbing_Log
        fields = ['id', 'date_logged', 'profile', 'climb']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username']        

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    saved_gyms = serializers.HyperlinkedRelatedField(queryset=Gym.objects.all(),
                                                     many=True,
                                                     view_name='gym-detail')
    saved_walls = serializers.HyperlinkedRelatedField(queryset=Wall.objects.all(),
                                                      many=True,
                                                      view_name='wall-detail')
    saved_climbs = serializers.HyperlinkedRelatedField(queryset=Climb.objects.all(),
                                                       many=True,
                                                       view_name='climb-detail')
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'saved_gyms', 'saved_walls', 'saved_gyms', 'saved_climbs']

class CreateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user