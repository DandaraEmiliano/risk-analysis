from pymongo import MongoClient
from .logger_config import setup_logger

logger = setup_logger(__name__)

def load(df, db_name, collection_name):
    logger.info(f"Conectando ao MongoDB - Banco: {db_name}, Coleção: {collection_name}")
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    data = df.to_dict(orient="records")
    result = collection.insert_many(data)
    logger.info(f"{len(result.inserted_ids)} registros inseridos no MongoDB")
