import asyncio
import logging
import sys

import uvloop
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot.handlers import all_routers

from bot.core.config import settings

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def main() -> None:
    dp = Dispatcher()
    for router in all_routers:
        dp.include_router(router)

        bot = Bot(
        token=settings.telegram_bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )


    async def on_startup(bot: Bot):
        logging.info("Bot started")


    async def on_shutdown(bot: Bot):
        logging.info("Bot stopped")


    await dp.start_polling(
        bot,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        close_bot_session=True,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvloop.run(main())