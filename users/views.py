from django.shortcuts import render
from rest_framework import generics
from .models import Player, PlayerOption
from .serializers import PlayerSerializer, PlayerOptionSerializer
from .filters import PlayerFilter, PlayerOptionFilter


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_class = PlayerFilter


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerOption.objects.all()
    serializer_class = PlayerOptionSerializer
