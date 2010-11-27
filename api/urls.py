from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from api.handlers import StationHandler


stations = Resource(StationHandler)

urlpatterns = patterns('',
    url(r'^stations$', stations),
    url(r'^stations.(?P<id>\d+)$', stations),
    url(r'^stations\.(?P<emitter_format>.+)', stations, name='stations'),

    # automated documentation
    url(r'^$', documentation_view),
)