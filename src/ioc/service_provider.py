from dishka import Provider, Scope, provide


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    ...

