from django.db import models
from django import forms

# Create your models here.


class SerieField(models.CharField):
    def to_python(self, value):
        return value.upper()


class Camera(models.Model):
    nome      = models.CharField(max_length=50, default='nome')
    fabricante = models.CharField(max_length=50, default='fabricante')
    serie       = SerieField(max_length=16, default='serie')



    
#python 3
    def __str__(self):
       return self.nome
    
#python 2
    def __unicode__(self):
        return self.nome


