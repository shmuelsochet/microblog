import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    TEMPLATES_AUTO_RELOAD = os.getenv('TEMPLATES_AUTO_RELOAD') or True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    POSTS_PER_PAGE = os.getenv('POSTS_PER_PAGE') or 3
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['sysochetdev@gmail.com']
    LANGUAGES = ['en', 'es', 'he']
    MS_TRANSLATOR_KEY = os.getenv('MS_TRANSLATOR_KEY')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

