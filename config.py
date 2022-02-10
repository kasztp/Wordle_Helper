from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config:
    """ Config settings for Flask app. """
    SECRET_KEY = environ.get('SECRET_KEY') or 'nobody-gonna-guess-it'
    RECAPTCHA_PRIVATE_KEY = environ.get('RC_SECRET_KEY')
    RECAPTCHA_PUBLIC_KEY = environ.get('RC_PUBLIC_KEY')
    STATIC_PATH = './app/static'
    DEBUG = False
