"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """
import os

class Config(object):

    from dotenv import load_dotenv
    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(APP_ROOT, '.env.local')
    load_dotenv(dotenv_path)

    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV')
    # if (FLASK_ENV):
    #     raise Exception('Environment varriable FLASK_ENV not set: {}'.format(FLASK_ENV))

    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret-Party')
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')
    API_BASE = 'https://localost:5000/api'
    # Will check for a database URL in heroku OR default to an sqlite db
    if (FLASK_ENV == 'TESTING'):
        sqlite = 'sqlite:///' + os.path.join(ROOT_DIR, 'tests', 'db.sqlite')
    else:
        sqlite = 'sqlite:///' + os.path.join(ROOT_DIR, 'app', 'db.sqlite')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', sqlite)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Basic Auth for Flask Admin
    BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD')

    # Slack API
    # SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN']
    SLACK_BOT_USER_OAUTH_TOKEN = os.getenv('SLACK_BOT_USER_OAUTH_TOKEN')
    SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

    # Celery
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")

    # Twilio
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {} Vue.js did not build the frontend.'.format(DIST_DIR))

    # # Override the default settings
    # if (FLASK_ENV == 'production') {
    #     API_BASE = 'https://rs-faces.herokuapp.com/api'
    # }