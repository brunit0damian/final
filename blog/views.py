from django.shortcuts import render, HttpResponse

def mi_vista(request):
    return HttpResponse("<h1>La pagina de Brunito</h1>")

# Create your views here.
