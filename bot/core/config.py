from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
        case_sensitive=False,
    )


class TelegramSettings(EnvBaseSettings):
    BOT_TOKEN: str


class GroqSettings(EnvBaseSettings):
    GROQ_API_KEY: str
    GROQ_MODEL: str
    GROQ_TEMPERATURE: float
    GROQ_MAX_TOKENS: int


class Settings(TelegramSettings, GroqSettings):
    DEBUG: bool = False


settings = Settings()
