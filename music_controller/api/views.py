from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins, viewsets
from .serializers import RoomSerializer, AppUserSerializer
from .models import Room, AppUser

# etoor what is the diff bw ListAPIView and CreateApiView

class RoomViewSet(generics.ListAPIView): 
    queryset = Room.objects.all() 
    serializer_class = RoomSerializer

class AppUserViewSet(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    viewsets.GenericViewSet
    ):
    queryset = AppUser.objects.all() 
    serializer_class = AppUserSerializer