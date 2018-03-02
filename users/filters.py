from django_filters import rest_framework as filters
from .models import Player, PlayerOption


class PlayerFilter(filters.FilterSet):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerOptionFilter(filters.FilterSet):
    class Meta:
        model = PlayerOption
        fields = '__all__'
