import asyncio
import logging
import os
import sys
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from groq import AsyncGroq
from bot.prompts import load_system_prompt

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

groq_client = AsyncGroq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = load_system_prompt()

async def generate_content(user_input: str) -> str:
    try:
        chat_completion = await groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1500,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"{str(e)}"
    
async def main() -> None:
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start_handler(message: Message) -> None:
        await message.answer(
            "Привет! *Я AI Dungeon Master, твой помощник для ролевой игры Dungeons & Dragons.* \n\n"
            "Опиши, что нужно для игры: сгенерировать сюжет, персонажа, квест или диалог. \n\n"
            "_Например: «Создай эльфа-мага с небольшой предисторией и распиши его характеристики»._",
            parse_mode=ParseMode.MARKDOWN_V2
            )

    @dp.message(F.text)
    async def dnd_handler(message: Message) -> None:
        user_input = message.text
        ai_response = await generate_content(user_input)
        await message.answer(ai_response)

    @dp.message()
    async def media_handler(message: Message) -> None:
        await message.answer("Я принимаю только текстовые сообщения.")


    async def on_startup(bot: Bot):
        logging.info("Bot started")


    async def on_shutdown(bot: Bot):
        logging.info("Bot stopped")


    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    await dp.start_polling(
        bot,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvloop.run(main())