from pymongo import MongoClient
from connection import DBConfig

url = DBConfig("mongodb").get_connection_url_mongodb()

client = MongoClient(url)
print("Connection successful")
mock = {"id": 1, "value": 123}
db = client.crypto_db
collection = db.btc
collection.insert_one(mock)

cursor = collection.find()
for record in cursor: 
    print(record)
