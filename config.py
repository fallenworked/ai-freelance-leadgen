from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
    TELEGRAM_CHAT_ID: int = 123456789  # Ваш Telegram ID или ID канала
    OPENAI_API_KEY: str = "sk-proj-YOUR_OPENAI_API_KEY_HERE"
    
    CHECK_INTERVAL_SECONDS: int = 60  # Интервал проверки новых заказов (сек)

    class Config:
        env_file = ".env"

settings = Settings()
