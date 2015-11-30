from django.conf.urls import patterns, include, url

urlpatterns = patterns('uthhconf.web.views',
    url(r'^', 'home', name='home_url'),
)
