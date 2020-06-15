from django.conf.urls import url
from django.urls import path
from . import views

app_name = "desafio"

urlpatterns = [
    url(r'$^', views.homePage),
    url(r'^add/', views.add, name='add'),
    url(r'^list/', views.list, name='list'),
    url(r'^remove/', views.remove, name='remove'),
    path('removeCamera/<int:id>', views.removeCamera, name='removeCamera'),
]
