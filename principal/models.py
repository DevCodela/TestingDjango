from django.db import models
from django.core.urlresolvers import reverse
from tastypie.utils.timezone import now
from django.contrib.auth.models import User

class Editor(models.Model):
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=60)
	provincia = models.CharField(max_length=30)
	pais = models.CharField(max_length=50)
	website = models.URLField()

	class Meta:
		ordering = ["-nombre"]

	def __str__(self):             
		return self.nombre

class Autor(models.Model):
	nombre = models.CharField(max_length=200)
	email = models.EmailField()
	def __str__(self):              
		return self.nombre

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autor = models.ForeignKey(Autor)
	editor = models.ForeignKey(Editor)
	fecha_publicacion = models.DateField(auto_now=True)
	puntuacion=models.IntegerField()

	def __str__(self):              
		return self.titulo

	def get_puntuacion(self):
		return self.puntuacion

