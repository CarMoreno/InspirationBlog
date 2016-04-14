from django.conf.urls import include, url
from . import views #Le decimos a Django que de este directorio importe el fichero views

urlpatterns = [
    url( r'^$' , views.books, name='index' ),
    # url( r'^books/$', views.books, name='all-books'),
    url(r'^books/(\d+)/$', views.detail_book, name='detail-book'),
    #Subir libros
	url(r'^crear-libro$', views.LibroCreateView.as_view(), name='crear'),
	#Update Libros
	url(r'^(?P<pk>\d+)/update-libro$', views.LibroUpdateView.as_view(), name='update'),
	#Delete Libros
	url(r'^(?P<pk>\d+)/delete-libro$', views.LibroDeleteView.as_view(), name='delete'),
]