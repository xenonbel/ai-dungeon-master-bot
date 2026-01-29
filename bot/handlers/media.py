from aiogram import Router
from aiogram.types import Message

router = Router(name="media_handler")

@router.message()
async def media_handler(message: Message) -> None:
    await message.answer("Я принимаю только текстовые сообщения.")