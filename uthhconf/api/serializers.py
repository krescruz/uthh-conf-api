from rest_framework import serializers

from .models import Equipo, Comentario

class EquipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Equipo


class ComentarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comentario
