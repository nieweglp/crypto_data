from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ddl import Base, FactPrice
from connection import DBConfig
from datetime import datetime


def main():
    url_postgres = DBConfig("postgres").get_connection_url_postgress()
    engine = create_engine(url_postgres)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)
    session.commit()

    url_mongodb = DBConfig("mongodb").get_connection_url_mongodb()
    client = MongoClient(url_mongodb)
    db = client.crypto_db
    collection = db.btc
    cursor = collection.find()
    # collection.drop()

    for data in cursor:
        print(data)
        fact_price = FactPrice(
            id=None,
            fetched_timestamp=data["fetched_timestamp"],
            insert_timestamp=datetime.now(),
            coin=data["base"],
            fiat_currency=data["currency"],
            price=data["amount"],
        )
        session.add(fact_price)
        session.commit()

    session.close()
    cursor.close()


if __name__ == "__main__":
    main()
