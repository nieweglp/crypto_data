from src.app.connection import DBConfig


def test_get_connection_url_postgres():
    result = DBConfig("postgres").get_connection_url_postgress()
    assert result == "postgresql://admin:admin@localhost:6543/crypto_db"

def test_get_connection_url_mongodb():
    result = DBConfig("mongodb").get_connection_url_mongodb()
    assert result == "mongodb://admin:admin@localhost:27017/"
