from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode

router = Router(name="start_handler")

@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "Привет! *Я AI Dungeon Master, твой помощник для ролевой игры Dungeons & Dragons.* \n\n"
        "Опиши, что нужно для игры: сгенерировать сюжет, персонажа, квест или диалог. \n\n"
        "_Например: «Создай эльфа-мага с небольшой предисторией и распиши его характеристики»._",
        parse_mode=ParseMode.MARKDOWN
    )