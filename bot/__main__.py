import logging

import uvloop
from aiogram import Bot

from bot.core.loader import create_bot
from bot.handlers import get_handlers_routers


async def on_startup(bot: Bot) -> None:
    logging.info("Bot started")

async def on_shutdown(bot: Bot) -> None:
    logging.info("Bot stopped")
    await bot.session.close()

async def main() -> None:
    bot, dp = create_bot()
    dp.include_router(get_handlers_routers())

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot)


if __name__ == "__main__":
#   logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvloop.run(main())
