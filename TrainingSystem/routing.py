from channels.auth import AuthMiddlewareStack
from channels.security.websocket import OriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': OriginValidator(
        # 'websocket':
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            ),
        ), ["https://pacific-garden-57867.herokuapp.com/"],
    )
})
