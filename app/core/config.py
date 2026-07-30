"""
Configuração global do PetPals.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    DEBUG: bool

    DATABASE_URL: str

    OLLAMA_HOST: str
    OLLAMA_MODEL: str

    LOG_LEVEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
