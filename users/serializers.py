from rest_framework import serializers
from .models import Player, PlayerOption


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerOption
        fields = '__all__'
