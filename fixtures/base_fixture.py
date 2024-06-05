import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# we imported expected_conditions and rename it to EC for easy use
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# we created and importing LoginPage from pages/login.py for make our code clear
from pages.login import LoginPage


class AdminLoginFixture(unittest.TestCase):
    # create a variable for ease use it in next code instead two parameters only one
    welcome_message_element = (By.ID, 'welcome')

    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')
        # here we use imported LoginPage fom ease using and make our code clear
        self.login_page = LoginPage(self.browser)
        # instead of next 4 strings of code
        # browser = self.browser
        # browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        # browser.find_element(By.ID, 'txtPassword').send_keys('password')
        # browser.find_element(By.ID, 'btnLogin').click()
        #
        self.login_page.authenticate()
        #
        self.login_page.wait_for_successful_login()
        # create a variable instead time.sleep(2)
        # add self before browser for using imported LoginPage
        self.wait = WebDriverWait(self.browser, 5)
        # time.sleep(2)

        # we use here only two parameters instead three, because we create welcome_message_element with two parameters
        # wait and return a value that is not False
        # EC - expected_conditions, presence_of_element_located - where the element is location, welcome_message_element
        # - message of the element
        # self.wait.until(EC.presence_of_element_located(self.welcome_message_element))
        # OR
        # wait and return a value that is not False where expected condition contains name of page
        # self.wait.until(EC.url_contains('/pim/viewEmployeeList'))

    def tearDown(self):
        self.browser.quit()