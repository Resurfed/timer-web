from django.shortcuts import render
from rest_framework import generics
from .models import Time, Server
from .serializers import TimeSerializer, ServerSerializer
from .filters import TimeFilter, ServerFilter


class TimeList(generics.ListCreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    filter_class = TimeFilter


class TimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_class = ServerFilter


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
