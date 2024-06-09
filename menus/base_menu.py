from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests import DEFAULT_WAIT


class BaseMenu:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)
        self.actions = ActionChains(self.browser)