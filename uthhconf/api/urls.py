from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('uthhconf.api.views',
    url(r'^', 'home', name='home_url'),
)
