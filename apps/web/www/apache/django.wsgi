import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'adscientiawww.configs.production.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()