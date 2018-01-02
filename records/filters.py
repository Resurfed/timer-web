from django_filters import rest_framework as filters
from .models import Time, Server


class TimeFilter(filters.FilterSet):
    class Meta:
        model = Time
        fields = '__all__'


class ServerFilter(filters.FilterSet):
    class Meta:
        model = Server
        fields = '__all__'
