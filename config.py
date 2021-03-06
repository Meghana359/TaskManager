from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """ Set Parent Class config variables """
    SECRET_KEY = environ['SECRET_KEY'] or "very_secret_key_1234567"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.sqlite3'


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.sqlite3'
