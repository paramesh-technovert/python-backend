# Usually empty unless you want to initialize something for the package
from app.config import settings
from app.routes import router as api_router

__all__ = ["settings", "api_router"]
