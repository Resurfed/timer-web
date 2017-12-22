from django_filters import rest_framework as filters
from .models import Map, Zone


class MapFilter(filters.FilterSet):
    min_difficulty = filters.NumberFilter(name="difficulty", lookup_expr='gte')
    max_difficulty = filters.NumberFilter(name="difficulty", lookup_expr='lte')

    class Meta:
        model = Map
        fields = '__all__'


class ZoneFilter(filters.FilterSet):
    class Meta:
        model = Zone
        fields = '__all__'