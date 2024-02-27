"""
ASGI config for feed_subscription_finrise project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import core.routing
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from feed_subscription_finrise.token_auth_middleware import JwtAuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'feed_subscription_finrise.settings')

asgi_application = get_asgi_application()  # new


application = ProtocolTypeRouter({
    "websocket": JwtAuthMiddlewareStack(URLRouter(core.routing.websocket_urlpatterns)),
})
