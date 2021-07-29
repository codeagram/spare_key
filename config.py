import os


class Config:

    SECRET_KEY = os.urandom(128)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class ProdConfig(Config):

        pass


class DevConfig(Config):

    DEBUG = True
    TESTING = True
