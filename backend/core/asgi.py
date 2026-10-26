"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application

# new import
from django_mcp import mount_mcp_server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# initialize django
django.setup()

# application = get_asgi_application()

# get the django http application
django_http_app = get_asgi_application()

# Mount MCP server dynamically using a URL parameter (e.g., user_uuid)
# application = mount_mcp_server(django_http_app=django_http_app, mcp_base_path='/mcp/<slug:user_uuid>')
application = mount_mcp_server(django_http_app=django_http_app, mcp_base_path='/mcp')

