import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from lib.browser import get_browser
from pages.add_employee import AddEmployee
from pages.employee_list import EmployeeList
from pages.login import LoginPage
from pages.pages.personal_details import PersonalDetails
from tests import DEFAULT_WAIT, DOMAIN


class BrowserFixture(unittest.TestCase):
    def setUp(self):
        self.browser = get_browser()
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

    def tearDown(self):
        self.browser.quit()


class AdminLoginFixture(BrowserFixture):
    welcome_message_element = (By.ID, 'welcome')

    def setUp(self):
        super().setUp()
        # self.browser.get(DOMAIN)
        self.login_page = LoginPage(self.browser)
        self.employee_list = EmployeeList(self.browser)
        self.add_employee = AddEmployee(self.browser)
        self.personal_details = PersonalDetails(self.browser)


        self.login_page.go_to_page()
        self.login_page.authenticate()
        self.login_page.wait_for_successful_login()
        # self.wait.until(EC.presence_of_element_located(self.welcome_message_element))
        # OR
        # self.wait.until(EC.url_contains('/pim/viewEmployeeList'))