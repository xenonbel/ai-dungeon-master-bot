import uvloop
from loguru import logger

from bot.core.loader import bot, dp
from bot.handlers import get_handlers_routers


async def on_startup() -> None:
    dp.include_router(get_handlers_routers())

    bot_info = await bot.get_me()

    logger.info(f'Name     - {bot_info.full_name}')
    logger.info(f'Username - @{bot_info.username}')
    logger.info(f'ID       - {bot_info.id}')

    states: dict[bool | None, str] = {
        True: 'Enabled',
        False: 'Disabled',
        None: "Unknown (This's not a bot)",
    }

    logger.info(f'Groups Mode  - {states[bot_info.can_join_groups]}')
    logger.info(f'Privacy Mode - {states[not bot_info.can_read_all_group_messages]}')
    logger.info(f'Inline Mode  - {states[bot_info.supports_inline_queries]}')

    logger.info('Bot started')


async def on_shutdown() -> None:
    await bot.session.close()

    logger.info('Bot stopped')


async def main() -> None:
    logger.add(
        'logs/telegram_bot.log',
        level='DEBUG',
        format='{time} | {level} | {module}:{function}:{line} | {message}',
        rotation='100 KB',
        compression='zip',
    )

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot)


if __name__ == '__main__':
    uvloop.run(main())
