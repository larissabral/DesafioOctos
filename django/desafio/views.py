from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm, AddForm
from django.views.generic import ListView


# Create your views here.

def homePage(request):
   return render(request, "desafio/index.html")

def list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "desafio/list.html", context)


def add(request):
    form = AddForm()
    if(request.method == 'POST'):
        form = AddForm(request.POST)
        if(form.is_valid()):
            post_nome = form.cleaned_data['nome']
            post_fabricante = form.cleaned_data['fabricante']
            post_serie = form.cleaned_data['serie']
            new_post = Post(nome=post_nome, fabricante=post_fabricante, serie=post_serie)
            new_post.save()
            return redirect('desafio:list')
    elif(request.method == 'GET'):
        return render(request, 'desafio/add.html', {'form': form})



def remove(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "desafio/remove.html", context)


def removeCamera(request, id):
    obj = get_object_or_404(Post, pk=id)
    obj.delete()
    return redirect('desafio:remove')
