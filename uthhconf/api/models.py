from django.db import models


class Equipo(models.Model):
	nombre = models.CharField(max_length=20, unique=True)
	url_avatar = models.URLField()

	def __str__(self):
		return self.nombre

class Comentario(models.Model):
	equipo = models.ForeignKey(Equipo)
	comentario = models.CharField(max_length=15)
	publicado = models.DateTimeField(auto_now=True)
	privado = models.BooleanField(default=False)
