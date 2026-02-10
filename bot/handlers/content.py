from aiogram import F, Router
from aiogram.types import Message

from bot.core.groq import generate_content

router = Router(name="content_handler")

@router.message(F.text)
async def dnd_handler(message: Message) -> None:
    user_input = message.text
    ai_response = await generate_content(user_input)
    await message.answer(ai_response)
