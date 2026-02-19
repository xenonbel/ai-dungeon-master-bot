from aiogram import Router

from . import content, media, start


def get_handlers_routers() -> Router:
    router = Router()

    router.include_router(start.router)
    router.include_router(content.router)
    router.include_router(media.router)

    return router
