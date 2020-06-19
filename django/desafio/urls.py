from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "desafio"

urlpatterns = [
    path('', views.home_page, name='index'),
    path('add/', views.add, name='add'),
    path('list/', views.list, name='list'),
    path('remove/', views.remove, name='remove'),
    path('removeCamera/<int:id>', views.remove_camera, name='removeCamera'),

#API 
    path('cameras/', views.CameraList.as_view()),
    path('cameras/<int:pk>/', views.CameraDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)