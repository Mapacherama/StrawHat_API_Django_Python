import os

import dotenv
dotenv.load_dotenv()

class Config(object):
    DEBUG = False
    FLASK_APP = os.environ.get("FLASK_APP")

    DATABASE_URL = os.environ.get("DATABASE_URL")
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE_ENGINE = os.environ.get("DATABASE_ENGINE")

    SERVER_NAME = os.environ.get("SERVER_NAME")

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True