"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import newrelic.agent
import os

newrelic.agent.initialize('/home/ubuntu/Project_8-OpenClassrooms/newrelic.ini')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.__init__") 

from django.core.wsgi import get_wsgi_application 

application = get_wsgi_application()
application = newrelic.agent.wsgi_application()(application)
