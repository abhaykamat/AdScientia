# Common URLs

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()


urlpatterns = patterns('',
    (r'^as_admin/', include(admin.site.urls)),
)

# Home
urlpatterns += patterns('adscientiawww.core.home.views',
    url(r'^/?$', 'viewHome', name='home_home'),
)

# Degrees
urlpatterns += patterns('adscientiawww.core.degrees.views',
    url(r'^degrees/(?P<degree>[A-Za-z0-9]+)/?$', 'viewDegrees', name='degrees_degree'),
)
