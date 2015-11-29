from django.http.response import HttpResponse

from rest_framework import viewsets

from .models import Equipo, Comentario
from .serializers import EquipoSerializer, ComentarioSerializer


class EquipoViewSet(viewsets.ModelViewSet):
	queryset = Equipo.objects.all()
	serializer_class = EquipoSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer
