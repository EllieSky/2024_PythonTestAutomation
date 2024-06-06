import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pc_pages.pc_login import LoginPage


class AdminLoginFixture(unittest.TestCase):
    def setUp(self, username='admin', password='password'):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')

        self.login = LoginPage(self.browser)
        self.login.autenticate()


    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
