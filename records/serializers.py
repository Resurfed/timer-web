from rest_framework import serializers
from .models import Time


class TimeSerializer(serializers.ModelSerializer):
    player_name = serializers.SerializerMethodField()
    map_name = serializers.SerializerMethodField()

    def get_player_name(self, obj):
        return obj.player.name

    def get_map_name(self, obj):
        return obj.map.name

    class Meta:
        model = Time
        fields = '__all__'
