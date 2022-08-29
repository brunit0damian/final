from enum import auto
from venv import create
from django.shortcuts import get_object_or_404, render, redirect #importamos metodo para construir plantillas
from .models import Post #importamos el modelo Post de donde sacamos datos
from django.utils import timezone #importamos timezone para que nos muestre la hora exacta en caso de un defauld
from .forms import PostCreateForm
from django.views.generic import View

#funcion de vista
def post_lista(request):                       #QuerySet
    posts = Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('fecha_de_publicacion') #sacamos todas las intancias de Post y la ordenamos por su fecha de publicacion y la guardamos en una variable
    return render(request, 'blog/post_lista.html', {'post': posts}) #request es la peticion URL del usuario y entre {} ponemos a mostrar los datos que queremos    

def post_lista2(request):
    return render(request, 'blog/post_lista2.html')

def principal(request): #funcion a renderizar mi plantilla de bootstrap
    return render(request, 'blog/principal.html') 

class blog_adelante(View):
    def get(self, request, *arg, **kwargs):
        new_post=PostCreateForm
        return render(request, 'blog/posteo_adelante.html', {'new_post': new_post})    

    def post(self, request, *arg, **kwargs):
        if request.method=="POST":
            new_post=PostCreateForm(request.POST)
            if new_post.is_valid():
                autor = new_post.cleaned_data.get('autor')
                titulo = new_post.cleaned_data.get('titulo')
                texto = new_post.cleaned_data.get('texto')
                fecha_de_creacion = new_post.cleaned_data.get('fecha_de_creacion')
                fecha_de_publicacion = new_post.cleaned_data.get('fecha_de_publicacion')
                p, create = Post.objects.get_or_create(auto=autor, titulo=titulo, texto=texto, fecha_de_creacion=fecha_de_creacion, fecha_de_publicacion=fecha_de_publicacion)
                p.save()
                return render(request, 'blog/posteo_adelante.html', {'new_post': new_post})            
