import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

APP_DEBUG = os.getenv('APP_DEBUG') == 'True'
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')
AWS_ACCOUNT_ID = os.getenv('AWS_ACCOUNT_ID')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_QUICKSIGHT_USER_EMAIL = os.getenv('AWS_QUICKSIGHT_USER_EMAIL')
FLASK_ENV = os.getenv('FLASK_ENV', 'production')
