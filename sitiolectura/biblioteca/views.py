from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from biblioteca.models import Editor, Autor, Libro
from django.views.generic.edit import CreateView, UpdateView, DeleteView#Vistas genericas de Django
from biblioteca.forms import FormCrearLibro
# Create your views here.

def primer_vista(request):
	return HttpResponse("Hola, soy tu primera vista")

def books(request):
	all_books = Libro.objects.all()
	context = {'object_list':all_books}
	return render(request, 'biblioteca/allbooks.html', context)

def detail_book(request, id_book):
	book = Libro.objects.get(id=id_book)
	context = {'object':book}
	return render(request, 'biblioteca/detailbook.html', context)

#----------------Vistas genericas------------
class LibroCreateView(CreateView):
	model = Libro
	form_class = FormCrearLibro #Caracteristicas especiales para este formulario
	template_name = 'biblioteca/uc_libro.html'

class LibroUpdateView(UpdateView):
	"""Clase-Vista generica que mostrara los datos de un libro para que este sea editado"""
	model = Libro
	form_class = FormCrearLibro
	template_name = 'biblioteca/uc_libro.html'	


class LibroDeleteView(DeleteView):
	model = Libro
	success_url = reverse_lazy('sitio:index')#Hacia donde me redirige despues de eliminar un libro