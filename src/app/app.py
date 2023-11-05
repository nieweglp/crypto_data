from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ddl import Base, DBConfig, FactPrice
from kafka import KafkaConsumer
import json
from datetime import datetime


def main():
    url = DBConfig().get_connection_url()
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)
    session.commit()

    consumer = KafkaConsumer(
        "crypto-stream",
        bootstrap_servers=["localhost:9092"],
        value_deserializer=lambda m: json.loads(m.decode("ascii")),
    )

    for message in consumer:
        data = message.value["data"]
        print(data)
        fact_price = FactPrice(
            id=None,
            timestamp=datetime.now(),
            coin=data["base"],
            fiat_currency=data["currency"],
            price=data["amount"],
        )
        print(fact_price)
        session.add(fact_price)
        session.commit()


if __name__ == "__main__":
    main()
