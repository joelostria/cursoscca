from django import forms
from app.curso.models import Curso

class CursoRegistro(forms.ModelForm):
	class Meta:
		model=Curso
		fields=[
			'nombre',
			'descripcion',
			'imagen',

		]	
		labels={
			'nombre':'Nombre',
			'descripcion':'Descripcion',
			'imagen':'Imagen',
		}
		widgets={
			'nombre':forms.TextInput(),
			'descripcion':forms.TextInput(),
			'imagen':forms.FileInput()
		}