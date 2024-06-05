import os
from configparser import ConfigParser

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(TEST_DIR)

BROWSER = os.environ.get('BROWSER') or 'chrome'


config = ConfigParser()
config.read(os.path.join(PROJECT_DIR, 'config.ini'))


DEFAULT_WAIT = int(config.get('default', 'DEFAULT_WAIT'))
LONG_WAIT = DEFAULT_WAIT * 6

DOMAIN = config.get('default', 'DOMAIN')
BASE_URL = f'{DOMAIN}/symfony/we/index.php'

ADMIN_USER = config.get('default', 'ADMIN_USERNAME')
DEFAULT_PASSWORD = config.get('default', 'DEFAULT_ADMIN_PASSWORD')

