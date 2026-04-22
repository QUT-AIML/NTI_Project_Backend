import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_MASTER_URL = os.getenv('MONGODB_MASTER_URL')

config = Config()