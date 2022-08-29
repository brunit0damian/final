from django.urls import path #libreria para usar path en urlpatterns
from . import views #importo vistas
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import blog_adelante

#añado patrones de urls enlazados a vistas
urlpatterns = [
    path('r', views.post_lista, name='post_lista'), #le estoy diciendo que mi '' localhost me muestre la template 'views.post_list'
    path('', views.post_lista2, name='post_lista2'),
    path('principal', views.principal, name='principal'), #agrego url de mi plantilla descargada de bootstrap
    path('agregar/', blog_adelante.as_view(), name='agregar'),
]

urlpatterns += staticfiles_urlpatterns()