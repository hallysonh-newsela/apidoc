import os

from pydantic import BaseModel


class Settings(BaseModel):
    environment: str = os.getenv("ENVIRONMENT", "dev")
