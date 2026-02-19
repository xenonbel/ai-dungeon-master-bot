from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from groq import AsyncGroq

from bot.core.config import settings

bot = Bot(
    token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

groq_client = AsyncGroq(api_key=settings.GROQ_API_KEY)

dp = Dispatcher()
