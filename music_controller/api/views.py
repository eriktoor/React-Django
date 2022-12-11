from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from .serializers import RoomSerializer
from .models import Room 

# etoor what is the diff bw ListAPIView and CreateApiView

class RoomView(generics.ListAPIView): 
    queryset = Room.objects.all() 
    serializer_class = RoomSerializer
