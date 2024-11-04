from pydantic import BaseModel
from functools import lru_cache
from typing import Optional

class Settings(BaseModel):
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "volleyball_stats"
    secret_key: str = "your-secret-key-here"  # In production, use a secure key
    access_token_expire_minutes: int = 30

@lru_cache()
def get_settings():
    return Settings()