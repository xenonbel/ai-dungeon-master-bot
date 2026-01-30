import asyncio
import logging
import sys

import uvloop
from aiogram import Bot

from bot.core.loader import bot, dp
from bot.handlers import get_handlers_routers

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def on_startup(bot: Bot) -> None:
    logging.info("Bot started")
    routers = get_handlers_routers
    for router in routers:
        dp.include_router(router)

async def on_shutdown(bot: Bot) -> None:
    logging.info("Bot stopped")

async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvloop.run(main())
