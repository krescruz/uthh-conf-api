from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^api/', include('uthhconf.api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
)
