from django.urls import path
from . import views

app_name = "desafio"

urlpatterns = [
    path('', views.home_page, name='index'),
    path('add/', views.add, name='add'),
    path('list/', views.list, name='list'),
    path('remove/', views.remove, name='remove'),
    path('removeCamera/<int:id>', views.remove_camera, name='removeCamera'),
]
