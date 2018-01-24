from django.shortcuts import render
from rest_framework import generics
from .models import Time
from .serializers import TimeSerializer
from .filters import TimeFilter
from .mixins import TimeRetrieveModelMixin, TimeListModelMixin


class TimeList(TimeListModelMixin, generics.ListCreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    filter_class = TimeFilter


class TimeDetail(TimeRetrieveModelMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

