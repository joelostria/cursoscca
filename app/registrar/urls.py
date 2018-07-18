from django.conf.urls import url, include
from app.registrar.views import index_registrar,registrar_view,registro_list,registro_edit,registro_delete,RegistroList,RegistroCreate,RegistroUpdate,RegistroDelete,exito

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index_registrar,name='index'),
    url(r'^nuevo$', RegistroCreate.as_view(),name='crear_registro'),
    url(r'^listar$', login_required(RegistroList.as_view()),name='listar_registro'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(RegistroUpdate.as_view()),name='editar_registro'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(RegistroDelete.as_view()),name='eliminar_registro'),
    url(r'^exito', exito,name='exito'),
	#url(r'^eliminar/(?P<id_alumno>\d+)/$', registro_delete,name='eliminar_registro'),    

]