from dishka import make_async_container

from .gateway_provider import GatewayProvider
from .service_provider import ServiceProvider


container = make_async_container(ServiceProvider(), GatewayProvider())


__all__ = ('container', )
