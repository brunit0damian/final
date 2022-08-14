from django.contrib import admin
from .models import Post #importamos el modelo creado Post

admin.site.register(Post) #ahora el modulo admin tiene permiso para crear, modificar y eliminar Post