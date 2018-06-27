import os
from flask_compress import Compress
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD=True


    SECRET_KEY = SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SESSION_TYPE = 'filesystem'

    # file upload configs
    SLIDES = os.getcwd() + '/app/static/assets/img/slides/'
    STORIES = os.getcwd() + '/app/static/assets/img/stories/'
    STORY = os.getcwd() + '/app/static/assets/img/stories/https://www.tubayo.com/storyimg/' and os.getcwd() + '/app/static/assets/img/stories/https://tubayo.com/storyimg/'
    EXPERIENCES = os.getcwd() + '/app/static/assets/img/experiences/'
    SHOP = os.getcwd() + '/app/static/assets/img/shop/'
    FLYERS = os.getcwd() + '/app/static/assets/img/flyers/'
    ADVERTS = os.getcwd() + '/app/static/assets/img/adverts/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



    # flask-cache
    CACHE_TYPE = 'simple'

    #compress
    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500

    # sqlalchemy configuration
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="root",
        password="Tomfoss2077@",
        hostname="localhost",
        databasename="tubayodb",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # # sqlalchemy configuration
    # SQLALCHEMY_POOL_RECYCLE = 280
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    #     username="root",
    #     password="tubayotravel2018",
    #     hostname="localhost",
    #     databasename="tubayodb",
    # )
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True


    # email server
    # MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    # MAIL_PORT = 25
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = False
    # MAIL_DEBUG = False
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # MAIL_DEFAULT_SENDER = None
    # MAIL_MAX_EMAILS = None
    # MAIL_ASCII_ATTACHMENTS = False

    # MAIL_DEBUG = True
    # TESTING = False
    # MAIL_SUPPRESS_SEND = False
    # MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    # # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
    # #     ['true', 'on', '1']
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # TUBAYO_MAIL_SUBJECT_PREFIX = '[Tubayo]'
    # TUBAYO_MAIL_SENDER = 'Tubayo Admin <ssebaggalaq@gmail.com>'
    # TUBAYO_ADMIN = os.environ.get('TUBAYO_ADMIN')

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'ssebaggalaq@gmail.com'
    TUBAYO_ADMIN = ['ssebaggalaq@gmail.com', 'quinton.ssebaggala@gmail.com']

    # MAIL_DEFAULT_SENDER : default None
    # MAIL_ASCII_ATTACHMENTS : default False

    # pagination
    POSTS_PER_PAGE = 100

    # flask social
    SOCIAL_AUTH_USER_MODEL = 'app.data.models.User'

    WHOOSH_BASE = 'whoosh/base'

    # marshmallow
    # JSON_SORT_KEYS=False 

    # elastic
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    ELASTICSEARCH_URL='http://localhost:9200'

    # babel
    LANGUAGES = ['en', 'es']


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD=True


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = True

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

def configure_app(app):
	config_name = os.getenv('FLASK_CONFIGURATION', 'production')
	app.config.from_object(config[config_name]) # object-based default configuration
	app.config.from_pyfile('config.cfg', silent=True) # instance-folders FLASK_CONFIGURATION

	# Configure Compressing
	Compress(app)