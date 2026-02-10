from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

class Settings(EnvBaseSettings):
    BOT_TOKEN: str
    GROQ_API_KEY: str
    debug: bool = False

settings = Settings()
