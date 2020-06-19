from django import forms
from .models import Camera

class SerieField(forms.CharField):
    def to_python(self, value):
        return value.upper()

FABRICANTES = (
    ('', 'Selecione o fabricante...'),
    ('Secure Câmeras Inc', 'Secure Câmeras Inc'),
    ('Surveillance Cams LLC', 'Surveillance Cams LLC'),
    ('DigiEye Group', 'DigiEye Group'),
    ('CâmeraFi Inc', 'CâmeraFi Inc'),
    ('VidMasters Inc', 'VidMasters Inc')
)

class AddForm(forms.Form):
    nome = forms.CharField(label='Nome da Câmera:', max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'ex: Hall de Entrada.'}), required=True)
    serie = SerieField(label='Número de Série:', max_length = 16, widget=forms.TextInput(attrs={'placeholder': 'Apenas caracteres maiúsculos e números, sem espaço.'}), required=True)
    fabricante = forms.ChoiceField(widget = forms.Select(), label='Fabricante:', choices=FABRICANTES, required=True)
    