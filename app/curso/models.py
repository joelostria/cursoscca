from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Curso(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.TextField()
	imagen=models.FileField(upload_to='')
		