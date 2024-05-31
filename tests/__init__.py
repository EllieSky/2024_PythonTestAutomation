import os
from configparser import ConfigParser

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(TEST_DIR)

BROWSER = os.environ.get('BROWSER') or 'chrome'
TEST_ENV = os.environ.get('TEST_ENV') or 'default'

config = ConfigParser()
config.read(os.path.join(PROJECT_DIR, 'config.ini'))


DEFAULT_WAIT = int(config.get(TEST_ENV, 'DEFAULT_WAIT'))
LONG_WAIT = DEFAULT_WAIT * 6

DOMAIN = config.get(TEST_ENV, 'DOMAIN')
BASE_URL = f'{DOMAIN}/symfony/web/index.php'

ADMIN_USER = config.get(TEST_ENV, 'ADMIN_USERNAME')
DEFAULT_PASSWORD = config.get('default', 'DEFAULT_ADMIN_PASSWORD')