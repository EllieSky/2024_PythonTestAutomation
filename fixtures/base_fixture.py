import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.dtb_login_page import LoginPage


class AdminLoginFixture(unittest.TestCase):
    welcome_message_element = (By.ID, 'welcome')

    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')
        self.login_page = LoginPage(self.browser)
        self.login_page.authenticate()
        self.wait = WebDriverWait(browser,5)
        self.wait.until(EC.presence_of_element_located(self.welcome_message_element))
        #self.wait.until(EC.url_contains('/pim/viewEmployeeList'))

    def tearDown(self):
        self.browser.quit()