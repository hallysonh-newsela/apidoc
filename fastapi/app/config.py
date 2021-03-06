import logging
import os
from functools import lru_cache
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")


@lru_cache()
def get_settings():
    log.info("Loading config settings from the environment...")
    return Settings()
