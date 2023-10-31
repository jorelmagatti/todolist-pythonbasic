import logging
import ecs_logging
from pydantic import AnyUrl, RedisDsn
from pydantic_settings import BaseSettings


handler = logging.StreamHandler()
handler.setFormatter(ecs_logging.StdlibFormatter())

logging.basicConfig(handlers=[handler])

class Settings(BaseSettings):
    database_uri: str = ""
    root_path: str = ""

settings = Settings()

