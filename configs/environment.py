from functools import lru_cache
import os 

from pydantic import BaseSettings

@lru_cache()
def get_environment_file():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"

class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    API_NAME: str
    DEBUG_MODE: bool
    DATABASE_DIALECT: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    
    class Config:
        env_file = get_environment_file()
        env_file_encoding = "utf-8"
        
@lru_cache()
def get_environment_variables():
    return EnvironmentSettings()
    