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

# Home
urlpatterns += patterns('adscientiawww.core.static.views',
    url(r'^about/?$', 'view_about', name='static_about'),
)

# Degrees
urlpatterns += patterns('adscientiawww.core.degrees.views',
    url(r'^degrees/(?P<degree>[A-Za-z0-9\_]+)/?$', 'viewDegrees', name='degrees_degree'),
)

# Courses
urlpatterns += patterns('adscientiawww.core.courses.views',
    url(r'^courses/(?P<degree>[A-Za-z0-9\_]+)/(?P<course>[A-Za-z0-9\_]+)?$', 'view_course', name='courses_course'),
    url(r'^courses/(?P<degree>[A-Za-z0-9\_]+)/(?P<course>[A-Za-z0-9\_]+)/(?P<chapter>[A-Za-z0-9\_]+)?$', 'view_course_chapter', name='courses_course_chapter'),
)
