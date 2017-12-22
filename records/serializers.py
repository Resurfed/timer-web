from rest_framework import serializers
from .models import Time


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'
