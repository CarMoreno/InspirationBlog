from django.db import models
from django.core.urlresolvers import reverse

class Editor(models.Model):
	'''Un editor tiene un nombre, un domicilio, una ciudad, un estado, un pais y un sitio web'''
	nombre = models.CharField(max_length=30)#el atributo nombre tendra maximo 30 caracteres
	domicilio = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=60)
	estado = models.CharField(max_length=30)
	pais = models.CharField(max_length=50)#el atributo pais tendra maximo 50 caracteres
	website = models.URLField()

	def __unicode__(self):#__str__ para python 3
		return self.nombre

	def get_absolute_url(self):
		return reverse('sitio:index')
			
	class Meta:
		verbose_name_plural = 'Editores'	
#____________________________________________________________			
class Autor(models.Model):
	'''Un autor tiene un nombre, un apellido y un email'''
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=40)
	email = models.EmailField(blank=True)#La BBDD aceptara valores vacios para este atributo
	
	def __unicode__(self):#__str__ para python 3
		cadena = "%s %s" %(self.nombre, self.apellido)
		return cadena

	def get_absolute_url(self):
		return reverse('sitio:index')
			
	class Meta:
		verbose_name_plural = 'Autores'

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autores = models.ManyToManyField(Autor) # Un libro, puede ser escrito por muchos autores, y un autor puede escribir muchos libros (Relacion muchos a muchos entre libro y autor)
	editor = models.ForeignKey(Editor)	#Un editor puede distribuir muchos libros, pero un libro solo puede ser distribuido por un solo editor (Relacion uno a muchos entre libros y editor, tambien conocida como llave foranea)
	fecha_publicacion = models.DateField()
	portada = models.ImageField(upload_to = 'portadas/')#Crea una carpeta donde guarara las imagenes de las portadas, al final la imagen tendra que cargarse en: media/portadas/, eso lo veremos luego
	sinopsis = models.TextField(blank=True)
	
	def get_absolute_url(self):
		return reverse('sitio:index')
		
	def __unicode__(self):#__str__ para python 3
		return self.titulo
