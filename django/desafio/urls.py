from django.conf.urls import url
from . import views

app_name = "desafio"

urlpatterns = [
    url(r'$^', views.homePage),
    url(r'^add/', views.add, name='add'),
    url(r'^list/', views.list, name='list'),
    url(r'^remove/', views.remove, name='remove'),
]
