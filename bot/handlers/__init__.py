from . import content, media, start


def get_handlers_routers():
    return [
        start.router,
        content.router,
        media.router,
    ]
