import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config:

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(64)
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@localhost:5432/remindersapp"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = True


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True
    TESTING = True
