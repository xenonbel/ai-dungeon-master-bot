from groq import AsyncGroq

from bot.core.config import settings
from bot.prompts import load_system_prompt

groq_client = AsyncGroq(api_key=settings.GROQ_API_KEY)

async def generate_content(user_input: str) -> str:
    try:
        chat_completion = await groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": load_system_prompt("system_prompt")},
                {"role": "user", "content": user_input},
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1500,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"{str(e)}"
