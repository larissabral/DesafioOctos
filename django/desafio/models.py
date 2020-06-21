from django.db import models

# Create your models here.


class SerieField(models.CharField):
    def to_python(self, value):
        return value.upper()


class Camera(models.Model):
    FABRICANTES = (
        ('Secure Câmeras Inc', 'Secure Câmeras Inc'),
        ('Surveillance Cams LLC', 'Surveillance Cams LLC'),
        ('DigiEye Group', 'DigiEye Group'),
        ('CâmeraFi Inc', 'CâmeraFi Inc'),
        ('VidMasters Inc', 'VidMasters Inc')
    )

    nome = models.CharField(max_length=50, default='nome')
    fabricante = models.CharField(max_length=50,
                                  default='fabricante',
                                  choices=FABRICANTES)
    serie = SerieField(max_length=16, default='serie', unique=True)

    # python 3
    def __str__(self):
        return self.nome

    # python 2
    def __unicode__(self):
        return self.nome
