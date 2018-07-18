from django import forms

from app.registrar.models import Alumno

class RegistrarForm(forms.ModelForm):

	class Meta:
		model=Alumno

		fields=[
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'computadora',
		]
		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'edad': 'Edad',
			'telefono':'Telefono',
			'email':'Email',
			'computadora':'Computadora'
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'validate','type':'text'}),
			'apellidos':forms.TextInput(attrs={'class':'validate'}),
			'edad':forms.TextInput(attrs={'class':'validate'}),
			'telefono':forms.TextInput(attrs={'class':'validate'}),
			'email':forms.TextInput(attrs={'class':'validate',}),
			'computadora':forms.TextInput(attrs={'class':'validate'}),
		}