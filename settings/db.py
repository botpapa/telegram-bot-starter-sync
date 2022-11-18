"""
Initializing connection with MongoDB
"""
import pymongo

from settings import config
from settings.logger import log

if config.MONGODB_CONNECTION_URI is not None:
    client = pymongo.MongoClient(config.MONGODB_CONNECTION_URI)
    db = client[config.MONGODB_DATABASE_NAME]
    log.info(f'MongoDB [{config.MONGODB_DATABASE_NAME}] initialized')
else:
    client, db = None, None
    log.warning(f'[service] MongoDB URI is not defined')
