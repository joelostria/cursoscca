from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from app.curso.models import Curso
from app.curso.forms import CursoRegistro
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class index(ListView):
	model=Curso
	template_name='curso/index.html'

class Registrar(CreateView):
	model=Curso
	form_class=CursoRegistro
	template_name='curso/registrar.html'
	success_url=reverse_lazy('curso:index')

class Listar(ListView):
	model=Curso
	template_name='curso/listar.html'
		
