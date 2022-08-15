from django.urls import path #libreria para usar path en urlpatterns

from . import views #importo vistas

#añado patrones de urls enlazados a vistas
urlpatterns = [
    path('', views.post_list, name='post_list'), #le estoy diciendo que mi '' localhost me muestre la template 'views.post_list'
]