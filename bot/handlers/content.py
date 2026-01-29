from aiogram import Router, F
from aiogram.types import Message

from bot.core.config import settings
from bot.prompts import load_system_prompt
from groq import AsyncGroq

router = Router(name="content_handler")

groq_client = AsyncGroq(api_key=settings.groq_api_key)

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
    
@router.message(F.text)
async def dnd_handler(message: Message) -> None:
    user_input = message.text
    ai_response = await generate_content(user_input)
    await message.answer(ai_response)