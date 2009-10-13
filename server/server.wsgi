import os
import sys

sys.path.append('/dev/project/zeit')

os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
