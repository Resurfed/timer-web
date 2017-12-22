from django.contrib import admin
from .models import Map, Spawn, Zone, MapConfiguration


admin.site.register(Map)
admin.site.register(Spawn)
admin.site.register(Zone)
admin.site.register(MapConfiguration)
