"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

'''
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
'''



#https://github.com/miguelgrinberg/python-socketio/blob/main/docs/server.rst

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_example.settings")

from socketio import Middleware, WSGIApp
# from socketio_app.views import sio
from apps.notes.views import sio
django_app = get_wsgi_application()
application = Middleware(sio, django_app)

#
import eventlet
import eventlet.wsgi
eventlet.wsgi.server(eventlet.listen(('', 8000)), application)