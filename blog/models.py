from django.conf import settings #importamos para el atributo 


from django.db import models #importamos para habilitar SQL de DJANGO
from django.utils import timezone #importamos timezone para que nos ayude con los atributos a la hora de hacer una publicacion en default

#....
class Post(models.model): #la herencia significa que es un modelo de DJANGO, asi DJANGO sabe que debe guardarlo en la DATEBASE
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150) #CharField es para cuando queremos limitar el contenido y usamos max_length para definir su longuitud
    texto = models.TextField() #TextFiel es en codigo SQL agregar texto sin limite
    fecha_de_creacion = models.DateTimeField(defauld=timezone.now) #si no se le asigna una fecha toma el valor de la fecha actual
    fecha_de_publicacion = models.DateTimeField(blank=True, null= True) #por defecto viene en blanco

    def publicar(self):
        self.fecha_de_publicacion = timezone.now() #al momento de publicar lo hace con la hora actual
        self.save() #decimos que guarde los posteos

    def __str__(self):
        return self.titulo        




