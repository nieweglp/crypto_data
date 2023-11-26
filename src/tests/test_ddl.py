from src.app.ddl import DBConfig


def test_dbconfig():
    result = DBConfig().get_connection_url()
    assert result == "postgresql://admin:admin@localhost:6543/crypto_db"
