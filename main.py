import asyncio
import logging
import os
import sys
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from groq import Groq

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

groq_client = Groq(api_key=GROQ_API_KEY)

dp = Dispatcher()

def generate_content(user_input: str) -> str:
    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ты AI Dungeon Master для Dungeons & Dragons — настольной ролевой игры в жанре фэнтези. "
                        "На основе запроса пользователя генерируй сюжеты, характеристики персонажей,"
                        "диалоги и квесты в стиле Dungeon & Dragons. Будь креативным, но обязательно соблюдай"
                        "правила пятой редакции."
                    )
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1000,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"{str(e)}"
    
@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer("Привет! *Я AI Dungeon Master, твой помощник для ролевой игры Dungeons & Dragons.* \n\n" 
                        "Опиши, что нужно для игры: сгенерировать сюжет, персонажа, квест или диалог. \n\n"
                        "_Например: «Создай эльфа-мага с небольшой предисторией и распиши его характеристики»._")
    parse_mode=ParseMode.MARKDOWN_V2

@dp.message(F.text)
async def dnd_handler(message: Message) -> None:
    user_input = message.text
    ai_response = generate_content(user_input)
    await message.answer(ai_response)

@dp.message()
async def media_handler(message: Message) -> None:
    await message.answer("Я принимаю только текстовые сообщения.")

async def main() -> None:
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())