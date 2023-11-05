from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ddl import Base, DBConfig


def main():
    url = DBConfig().get_connection_url()
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(
        engine, Base.metadata.tables.values(), checkfirst=True)
    session.commit()


if __name__ == "__main__":
    main()
