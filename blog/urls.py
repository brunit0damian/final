from django.urls import path #libreria para usar path en urlpatterns

from . import views #importo vistas

#añado patrones de urls enlazados a vistas
urlpatterns = [
    path('a', views.post_lista, name='post_lista'), #le estoy diciendo que mi '' localhost me muestre la template 'views.post_list'
    path('', views.post_lista2, name='post_lista2'),
]
