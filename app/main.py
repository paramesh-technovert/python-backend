from fastapi import FastAPI
from app import api_router

app = FastAPI(title="FastAPI Utility App")

app.include_router(api_router)
