from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Alumno(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos=models.CharField(max_length=70)
	edad=models.IntegerField()
	telefono=models.CharField(max_length=12)
	email=models.EmailField()
	computadora=models.CharField(max_length=12)

	def __unicode__(self):
		return '{}'.format(self.nombre)
		