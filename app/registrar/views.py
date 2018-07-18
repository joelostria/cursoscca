from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# Create your views here.

from django.core.urlresolvers import reverse_lazy
from app.registrar.forms import RegistrarForm
from app.registrar.models import Alumno


def index_registrar(request):
	return render(request, 'registrar/index.html')

def registrar_view(request):
	if request.method == 'POST':
		form=RegistrarForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('registrar:index')
	else:
		form=RegistrarForm()

	return render(request,'registrar/registro_form.html',{'form':form})

def registro_list(request):
	registro = Alumno.objects.all().order_by('id')
	contexto = {'registros':registro}
	return render(request, 'registrar/registros_list.html',contexto)

def registro_edit(request,id_alumno):
		registro=Alumno.objects.get(id=id_alumno)
		if request.method=='GET':
			form=RegistrarForm(instance=registro)
		else:
			form=RegistrarForm(request.POST,instance=registro)
			if form.is_valid():
				form.save()
			return redirect('registrar:listar_registro')
		return render(request,'registrar/registro_form.html',{'form':form})
def registro_delete(request,id_alumno):
	registro = Alumno.objects.get(id=id_alumno)
	if request.method=='POST':
		registro.delete()
		return redirect('registrar:listar_registro')
	return render(request,'registrar/registro_delete.html',{'registrar':registro})

class RegistroList(ListView):
	#registro=Alumno
	model=Alumno
	template_name='registrar/registros_list.html'	
class RegistroCreate(CreateView):
	"""docstring for RegistroCreate"""
	model=Alumno
	form_class= RegistrarForm
	template_name='registrar/registro_form.html'
	success_url=reverse_lazy('registrar:listar_registro')
class RegistroUpdate(UpdateView):
	model=Alumno
	form_class= RegistrarForm
	template_name='registrar/registro_form.html'
	success_url=reverse_lazy('registrar:listar_registro')

class RegistroDelete(DeleteView):
	model=Alumno
	template_name='registrar/registro_delete.html'
	success_url=reverse_lazy('registrar:listar_registro')
	
def exito(request):
	return render(request,'registrar/exito.html')