from dataclasses import fields
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post #indicamos que modelo debe ser utilizado para crear el formulario
        fields = ('autor', 'titulo') #solo queremos mostrar esto 