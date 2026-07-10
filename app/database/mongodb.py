from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from app.core.config import settings
from app.core.logger import get_logger
logger = get_logger(__name__)
try : 
    client = MongoClient(settings.MONGODB_URI)
    client.admin.command('ping')  # Check if the connection is successful
    logger.info(
    "Successfully connected to MongoDB. Database=%s Collection=%s",
    settings.DATABASE_NAME,
    settings.COLLECTION_NAME)
except ConnectionFailure as e:
    logger.error("Failed to connect to MongoDB: %s", str(e))
    raise

database = client[settings.DATABASE_NAME]


def get_incident_collection():
    """
    Return the MongoDB collection used to store incidents.
    """
    return database[settings.COLLECTION_NAME]