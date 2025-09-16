from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27018")
DB_NAME = "assessment_db"

client = AsyncIOMotorClient(MONGODB_URL)
database = client[DB_NAME]

def get_employee_collection():
    return database.employees
