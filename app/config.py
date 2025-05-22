#To store variables
import os
from dotenv import load_dotenv

# Load variables from .env if exists
load_dotenv()

class Settings:
    APP_NAME: str = "FastAPI App"
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

settings = Settings()