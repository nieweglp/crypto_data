from datetime import datetime
from kafka import KafkaConsumer
import json
from pymongo import MongoClient
from src.app.connection import DBConfig

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "crypto-stream",
        bootstrap_servers=["localhost:9092"],
        value_deserializer=lambda m: json.loads(m.decode("ascii")),
    )

    url = DBConfig("mongodb").get_connection_url_mongodb()

    client = MongoClient(url)
    print("Connection successful")
    db = client.crypto_db
    collection = db.btc

    for message in consumer:
        data = message.value["data"]
        data["fetched_timestamp"] = datetime.now()
        collection.insert_one(data)
    