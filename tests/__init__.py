import os
from configparser import ConfigParser

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(TEST_DIR)


BROWSER = os.environ.get('BROWSER') or 'chrome'
TEST_ENV = os.environ.get('TEST_ENV') or 'local'

config = ConfigParser()
config.read(os.path.join(PROJECT_DIR, 'config.ini'))


DEFAULT_WAIT = config.get('default', 'DEFAULT_WAIT')
LONG_WAIT = 30


DOMAIN = config.get('default',   'DOMAIN')
BASE_URL = f'{DOMAIN}/symfony/web/index.php'

ADMIN_USER = config.get('default', 'ADMIN_USER')
DEFAULT_ADMIN_PASSWORD = config.get('default', 'DEFAULT_ADMIN_PASSWORD')