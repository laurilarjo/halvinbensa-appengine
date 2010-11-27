from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^polls/', include('polls.urls')),
	(r'^api/', include('api.urls')),
	(r'^admin/', include('urlsadmin')),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
