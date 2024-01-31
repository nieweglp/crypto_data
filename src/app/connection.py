from configparser import ConfigParser


class DBConfig:
    config = ConfigParser()
    config.read("src/configs/config.ini")
    def __init__(self, database):
        self.DB_ENGINE = self.config.get(database, "DB_ENGINE")
        self.LOGIN = self.config.get(database, "LOGIN")
        self.PASSWORD = self.config.get(database, "PASSWORD")
        self.HOST = self.config.get(database, "HOST")
        self.PORT = self.config.get(database, "PORT")
        self.DB_NAME = self.config.get(database, "DB_NAME", fallback=0)

    def get_connection_url_postgress(self):
        url_str = (
            f"{self.DB_ENGINE}://"
            f"{self.LOGIN}:{self.PASSWORD}"
            f"@{self.HOST}:{self.PORT}/"
            f"{self.DB_NAME}"
        )
        return url_str
    
    def get_connection_url_mongodb(self):
        url_str = (
            f"{self.DB_ENGINE}://"
            f"{self.LOGIN}:{self.PASSWORD}"
            f"@{self.HOST}:{self.PORT}/"
        )
        return url_str
    