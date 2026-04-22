from motor.motor_asyncio import AsyncIOMotorClient
from app.config import config


client: AsyncIOMotorClient|None = None


async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(config.MONGODB_MASTER_URL)
    print("Connected to MongoDB")

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("MongoDB connection closed")

def get_db():
    global client
    if not client:
        raise Exception("MongoDB client is not initialized")
    return client[config.MONGODB_MASTER_URL]