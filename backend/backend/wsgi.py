"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#Check for env var to see if we're in Azure App Services
settings_module = 'projectapi.production' if 'WEBSITE_HOSTNAME' in os.environ else 'projectapi.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
