from rest_framework import serializers
from .models import Room, AppUser
from django.db import models
import string
import random 

from django.contrib.auth import get_user_model


class RoomSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Room 
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

class AppUserSerializer(serializers.ModelSerializer): 
    email = serializers.EmailField(source="user.email", required=False)
    first_name = serializers.CharField(source="user.first_name", required=False)
    last_name = serializers.CharField(source="user.last_name", required=False)

    class Meta: 
        model = AppUser 
        fields = ['email', 'first_name', 'last_name']

    def create(self, validatedData):
        # breakpoint() 
        User = get_user_model() 
        user = User.objects.create( 
            username = validatedData["user"]["email"],
            email = validatedData["user"]["email"], 
            first_name = validatedData["user"]["first_name"],
            last_name = validatedData["user"]["last_name"],
        )
        app_user = AppUser.objects.create(
            user=user
        )
        return app_user