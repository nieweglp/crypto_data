from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from dotenv import load_dotenv
import os


Base = declarative_base()


class FactPrice(Base):
    __tablename__ = "fact_spot_price"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime)
    coin = Column(String(3))
    fiat_currency = Column(String(3))
    price = Column(Float)


load_dotenv()


class DBConfig:
    def __init__(self):
        self.DB_ENGINE = os.getenv("DB_ENGINE")
        self.LOGIN = os.getenv("LOGIN")
        self.PASSWORD = os.getenv("PASSWORD")
        self.HOST = os.getenv("HOST")
        self.PORT = os.getenv("PORT")
        self.DB_NAME = os.getenv("DB_NAME")

    def get_connection_url(self):
        url_str = (
            f"{self.DB_ENGINE}://"
            f"{self.LOGIN}:{self.PASSWORD}"
            f"@{self.HOST}:{self.PORT}/"
            f"{self.DB_NAME}"
        )
        return url_str
