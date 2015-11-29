from django.conf.urls import patterns, include, url
from rest_framework import routers

from .views import (
	EquipoViewSet, ComentarioViewSet
)

router = routers.DefaultRouter()
router.register(r'equipos', EquipoViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = patterns('uthhconf.api.views',
    url(r'^', include(router.urls)),
)
