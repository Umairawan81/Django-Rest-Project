from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # Nmae of the model we want to serialize
        fields = ('id', 'username', 'password')  # name of the feilds of the above 
        # selected model to serialize
        extra_kwargs = {'password':{'write_only': True}} # THis willl ensure that upon 
        # returning user details password should not be returned.

    def create(self , validated_data):
        user = User.objects.create_user(**validated_data) # This will create a user after the validation
        # performed by UserSerializer
        user.save()
        return user
    

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id' , 'title' ,'content' ,'created_on' , 'author')
        extra_kwargs = {'author':{'read_only': True}}


