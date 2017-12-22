from django_filters import rest_framework as filters
from .models import Time


class TimeFilter(filters.FilterSet):
    class Meta:
        model = Time
        fields = '__all__'