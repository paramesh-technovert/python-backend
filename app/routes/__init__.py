# Optional import shortcuts if you want to organize routes
from fastapi import APIRouter
from app.routes.numberOperations import router as number_router
from app.routes.stringOperations import router as string_router

router = APIRouter()
router.include_router(number_router, prefix="/numbers", tags=["Number Operations"])
router.include_router(string_router, prefix="/strings", tags=["String Operations"])
