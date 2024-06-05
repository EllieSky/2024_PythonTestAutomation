from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests import DEFAULT_WAIT


class BasePage:
    PAGE_URL = None
    page_header = (By.CSS_SELECTOR, '.head>h1')
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, DEFAULT_WAIT)
    def go_to_page(self):
        self.browser.get(self.PAGE_URL)

    def get_page_header(self):
        self.browser.findelement(*self.page_header)