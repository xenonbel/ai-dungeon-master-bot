from .start import router as start_router
from .media import router as media_router
from .content import router as content_router 

all_routers = [
    start_router,
    content_router,
    media_router,
]