from django.shortcuts import render, HttpResponse #importo HttpResponse para que se me haga mas facil mostrar codigo HTML
def mi_vista(request):
    return HttpResponse("<h1>La pagina de Brunito</h1>")

# Create your views here.
