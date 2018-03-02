from rest_framework import serializers
from .models import Time


class TimeSerializer(serializers.ModelSerializer):
    player_name = serializers.SerializerMethodField()
    map_name = serializers.SerializerMethodField()
    rank = serializers.SerializerMethodField()
    completions = serializers.IntegerField(
        source='',
        read_only=True
    )

    def get_player_name(self, obj):
        return obj.player.name

    def get_map_name(self, obj):
        return obj.map.name

    def get_rank(self, obj):
        return obj.actual_rank()

    class Meta:
        model = Time
        fields = '__all__'

