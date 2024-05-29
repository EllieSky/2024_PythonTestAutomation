import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.login9 import LoginPage

class BrowserFixture(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.browser, 5)

    def tearDown(self):
        self.browser.quit()


class AdminLoginFixture(BrowserFixture):
    welcome_message_element = (By.ID, 'welcome')
    def setUp(self):
        # self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        super().setUp()
        self.browser.get('http://hrm-online.portnov.com/')
        browser = self.browser
        self.login_page = LoginPage(self.browser)
        self.login_page.authenticate()
        self.login_page.wait_for_succesful_login()
        # browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        # browser.find_element(By.ID, 'txtPassword').send_keys('password')
        # browser.find_element(By.ID, 'btnLogin').click()
        self.wait = WebDriverWait(self.browser,5)
        self.wait.until(EC.presence_of_element_located(self.welcome_message_element))
        # self.wait.until(EC.url_contains('/pim/viewEmployeeList'))

