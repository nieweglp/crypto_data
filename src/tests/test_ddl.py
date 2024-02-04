from src.app.ddl import FactPrice


def test_name():
    assert FactPrice.__tablename__ == "fact_spot_price"
