import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config:

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(64)
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://brtzdqrdjxljnt:154cecb747717cc481cdcfa5f063c63f05b34600d062b08208f2328afe483847@ec2-54-157-100-65.compute-1.amazonaws.com:5432/dar4i11itgigor"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = True


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True
    TESTING = True
