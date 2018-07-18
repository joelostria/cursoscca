from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from app.usuarios.forms import RegistroForm

class RegistroUsuario(CreateView):
 	model=User
 	template_name="usuario/registrar.html"
 	form_class=RegistroForm
 	success_url=reverse_lazy('registrar:exito')


# Create your views here.
