from pathlib import Path
from typing import List, Dict

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    APP_NAME: str = "py-template-api"
    PORT: int = 5000
    HOST: str = "localhost"

    APP_URIS: List[Dict[str, str]] = [
        {"url": "http://localhost:5000", "description": "DEV"}
    ]

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30

    DATABASE_DSN: PostgresDsn = None

    class Config:
        env_file = Path("../.env")


settings = Settings()

# templates = Jinja2Templates(directory="templates")
