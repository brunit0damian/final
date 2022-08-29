from dataclasses import fields
from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post #indicamos que modelo debe ser utilizado para crear el formulario
        fields = ('autor', 'titulo', 'texto', 'fecha_de_creacion', 'fecha_de_publicacion') #solo queremos mostrar esto 