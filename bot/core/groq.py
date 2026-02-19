from bot.core.config import settings
from bot.core.loader import groq_client
from bot.core.prompts import load_system_prompt


async def generate_content(user_input: str) -> str:
    try:
        chat_completion = await groq_client.chat.completions.create(
            messages=[
                {'role': 'system', 'content': load_system_prompt('system_prompt')},
                {'role': 'user', 'content': user_input},
            ],
            model=settings.GROQ_MODEL,
            temperature=settings.GROQ_TEMPERATURE,
            max_tokens=settings.GROQ_MAX_TOKENS,
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        return f'{str(e)}'
