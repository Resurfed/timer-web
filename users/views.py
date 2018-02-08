from django.shortcuts import render
from rest_framework import generics
from .models import Player, PlayerOption
from .serializers import PlayerSerializer, PlayerOptionSerializer
from .filters import PlayerFilter, PlayerOptionFilter
from rest_framework import filters


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'steam_id')
    filter_class = PlayerFilter



class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerOption.objects.all()
    serializer_class = PlayerOptionSerializer
