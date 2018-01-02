from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from records import views

urlpatterns = [
	path('', views.TimeList.as_view()),
	path('<int:pk>/', views.TimeDetail.as_view()),
	path('servers/', views.ServerList.as_view())
	path('servers/<int:pk>', views.ServerDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
