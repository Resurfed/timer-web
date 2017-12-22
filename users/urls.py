from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
	path('', views.PlayerList.as_view()),
	path('<int:pk>/', views.PlayerDetail.as_view()),
	path('<int:pk>/options/', views.PlayerOptionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
