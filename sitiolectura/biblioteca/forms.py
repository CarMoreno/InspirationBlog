from django import forms
from django.forms import ModelForm
from biblioteca.models import Libro, Autor, Editor


class FormCrearLibro(forms.ModelForm):
    class Meta:
        model = Libro
    	fields = ['titulo', 'autores', 'editor', 'fecha_publicacion', 'portada', 'sinopsis']
    	