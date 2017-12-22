from django.contrib import admin
from .models import Server, Time, Checkpoint


admin.site.register(Server)
admin.site.register(Time)
admin.site.register(Checkpoint)
