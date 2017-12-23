from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/', include('maps.urls')),
    path('players/', include('users.urls')),
    path('times/', include('records.urls')),
]
