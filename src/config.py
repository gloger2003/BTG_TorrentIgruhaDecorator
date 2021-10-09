import os


app_dir = os.path.abspath(os.path.dirname(__file__))

TORRENT_IGRUHA_DOMEN = 'https://s1.utorrentigruha.org/'


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A REAL LONG SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or \
        'mysql+pymysql://root@localhost/TorrentIgruha'


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
        'mysql+pymysql://root@localhost/TorrentIgruha'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
        'mysql+pymysql://root@localhost/flask_app_db'