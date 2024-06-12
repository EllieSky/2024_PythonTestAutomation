from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests import DEFAULT_WAIT


class BaseBlock:
    def __init__(self, browser):
        self.browser: WebDriver = browser
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)
