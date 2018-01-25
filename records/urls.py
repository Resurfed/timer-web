from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from records import views

urlpatterns = [
    path('api/', views.TimeList.as_view()),
    path('api/<int:pk>/', views.TimeDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
