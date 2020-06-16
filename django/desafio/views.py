from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Camera
from .forms import CameraForm, AddForm
from django.views.generic import ListView


# Create your views here.

def homePage(request):
   return render(request, "desafio/index.html")

def list(request):
    queryset = Camera.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "desafio/list.html", context)


def add(request):
    form = AddForm()
    if(request.method == 'POST'):
        form = AddForm(request.POST)
        if(form.is_valid()):
            camera_nome = form.cleaned_data['nome']
            camera_fabricante = form.cleaned_data['fabricante']
            camera_serie = form.cleaned_data['serie']
            if (Camera.objects.filter(serie=camera_serie).exists()):
               messages.success(request, 'Esse Número de Série já existe! Por favor entre com outro!')
               return redirect('desafio:add')
            else:
               new_camera = Camera(nome=camera_nome, fabricante=camera_fabricante, serie=camera_serie)
               new_camera.save()
               return redirect('desafio:list')
    elif(request.method == 'GET'):
        return render(request, 'desafio/add.html', {'form': form})



def remove(request):
    queryset = Camera.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "desafio/remove.html", context)


def removeCamera(request, id):
    obj = get_object_or_404(Camera, pk=id)
    obj.delete()
    return redirect('desafio:remove')
