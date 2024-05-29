from selenium.webdriver.support.wait import WebDriverWait
from tests import DEFAULT_WAIT


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, DEFAULT_WAIT)