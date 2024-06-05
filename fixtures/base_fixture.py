import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import LoginPage
class BrowserFixture(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.browser, 5)

    def tearDown(self):
        self.browser.quit()


class AdminLoginFixture(BrowserFixture):
    welcome_message_element = (By.ID, 'welcome')
    def setUp(self):
        super().setUp()
        self.browser.get('http://hrm-online.portnov.com/')
        self.login_page = LoginPage(self.browser)
        self.login_page.authenticate()
        self.login_page.wait_for_successful_login()
        # self.wait.until(EC.presence_of_element_located(self.welcome_message_element))
        # OR
        # self.wait.until(EC.url_contains('/pim/viewEmployeeList'))

    def tearDown(self):
        self.browser.quit()
        # self.wait.until(EC.url_contains('/pim/viewEmployeeList'))