from django.shortcuts import render #importamos metodo para construir plantillas
from .models import Post #importamos el modelo Post de donde sacamos datos
from django.utils import timezone #importamos timezone para que nos muestre la hora exacta en caso de un defauld

#funcion de vista
def post_lista(request):                       #QuerySet
    posts = Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('fecha_de_publicacion') #sacamos todas las intancias de Post y la ordenamos por su fecha de publicacion y la guardamos en una variable
    return render(request, 'blog/post_lista.html', {'post': posts}) #request es la peticion URL del usuario y entre {} ponemos a mostrar los datos que queremos    
def post_lista2(request):
    return render(request, 'blog/post_lista2.html')