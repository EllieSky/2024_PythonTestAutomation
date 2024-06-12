from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from lib.base_methods import BaseMethods
from tests import DEFAULT_WAIT


class BasePage(BaseMethods):
    PAGE_URL = None
    page_header = (By.CSS_SELECTOR, '.head>h1')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser: WebDriver = browser
        self.wait = WebDriverWait(browser, DEFAULT_WAIT)

    def go_to_page(self):
        self.browser.get(self.PAGE_URL)

    def get_page_header(self):
        self.browser.find_element(*self.page_header)