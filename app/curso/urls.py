from django.conf.urls import url
#from django.urls import path
from app.curso.views import index,Registrar,Listar
from . import views as uploader_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', index.as_view(),name='index'),
    url(r'^registrar', Registrar.as_view(),name='registrar_curso'),
    url(r'^listar', Listar.as_view(),name='listar_curso'),
    #url('', uploader_views.Listar, name='imageupload'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)