from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "py-template-api"
    PORT: int = 5000
    HOST: str = "localhost"

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = Path("../.env")


settings = Settings()

# templates = Jinja2Templates(directory="templates")
