from django.conf.urls.defaults import *
from api.models import Station

urlpatterns = patterns('stations.views',
    (r'^$', 'index'),
    (r'^all/$', 'all'),
    (r'^(?P<station_id>\d+)/$', 'details'),
)