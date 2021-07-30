import os


class Config:

    SECRET_KEY = "1815ca3ce169a5eb76f6f7165e9be31043514954f9db1f0341b48c0115e33d74f1ca1df1cc7cd6360c5139a257cec1bd2a78a368296abd7f52746e2bf1bcc582"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class ProdConfig(Config):

        pass


class DevConfig(Config):

    DEBUG = True
    TESTING = True
