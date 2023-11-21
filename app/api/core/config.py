from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

dotenv_path = Path(__file__).parents[2] / '.env'


class Settings(BaseSettings):
    """FastAPI settings."""
    # App
    APP_NAME: str = "Notes API"
    APP_DESCRIPTION: str = "Notes API using FastAPI"
    APP_VERSION: str = "0.0.1"
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000
    APP_RELOAD: bool = False
    APP_DEBUG: bool = True

    # Database
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    # API
    API_V1_URL: str = "/api/v1"
    API_DOCS_URL: str = "/api/v1/docs"

    # Auth
    SECRET_KEY: str

    class Config:
        case_sensitive = True
        env_file = dotenv_path


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
