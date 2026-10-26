# asgi.py
import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from django_mcp import mount_mcp_server  # must come after django.setup()

django_http_app = get_asgi_application()

# for django ASGI:
application = mount_mcp_server(django_http_app=django_http_app, mcp_base_path='/mcp')

# for django-channels ASGI:
# from channels.routing import ProtocolTypeRouter
# application = ProtocolTypeRouter({
#     "http": mount_mcp_server(django_http_app=django_http_app, mcp_base_path='/mcp')
# })