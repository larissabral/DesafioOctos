from django import forms
from .models import Camera

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['nome', 'fabricante', 'serie']


FABRICANTES = (
    ('', 'Selecione o fabricante...'),
    ('Secure Câmeras Inc', 'Secure Câmeras Inc'),
    ('Surveillance Cams LLC', 'Surveillance Cams LLC'),
    ('DigiEye Group', 'DigiEye Group'),
    ('CâmeraFi Inc', 'CâmeraFi Inc'),
    ('VidMasters Inc', 'VidMasters Inc')
)

class AddForm(forms.Form):
    nome = forms.CharField(label='Nome da Câmera:', max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'ex: Hall de Entrada.'}))
    serie = forms.CharField(label='Número de Série:', max_length = 16, widget=forms.TextInput(attrs={'placeholder': 'Apenas caracteres maiúsculos e números, sem espaço.'}))
    fabricante = forms.ChoiceField(label='Fabricante:', choices=FABRICANTES)
    
