from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.api import api_router
from app.config import config
from app.connection import connect_to_mongo, close_mongo_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    print("App started")

    yield  

    await close_mongo_connection()
    print("App stopped")

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)


