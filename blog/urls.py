from django.urls import path #libreria para usar path en urlpatterns

from . import views #importo vistas

#añado patrones de urls enlazados a vistas
urlpatterns = [
    path('', views.mi_vista, name='mi_vista')
]