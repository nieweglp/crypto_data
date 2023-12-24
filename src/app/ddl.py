from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float


Base = declarative_base()

class FactPrice(Base):
    __tablename__ = "fact_spot_price"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fetched_timestamp=Column(DateTime)
    insert_timestamp = Column(DateTime)
    coin = Column(String(3))
    fiat_currency = Column(String(3))
    price = Column(Float)
