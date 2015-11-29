# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.db import models


class Equipo(models.Model):
	
	alphanumeric_validator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos')

	nombre = models.CharField(max_length=20, unique=True, validators=[alphanumeric_validator])
	url_avatar = models.URLField()

	def __str__(self):
		return self.nombre

class Comentario(models.Model):
	equipo = models.ForeignKey(Equipo)
	comentario = models.CharField(max_length=15)
	publicado = models.DateTimeField(auto_now=True)
	privado = models.BooleanField(default=False)
