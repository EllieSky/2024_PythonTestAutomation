import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from lib.browser import get_browser
from menus.main_menu import MainMenu
from menus.user_menu import UserMenu
from pages.add_employee import AddEmployee
from pages.employee_list import EmployeeList
from pages.job_page import JobPage
from pages.login import LoginPage
from pages.personal_details import PersonalDetails
from pages.personal_details import PersonalDetails, MyInfo
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
        self.my_info = MyInfo(self.browser)
        self.job_page = JobPage(self.browser)

        self.user_menu = UserMenu(self.browser)
        self.main_menu = MainMenu(self.browser)

        self.login_page.go_to_page()
        self.login_page.authenticate()
        self.login_page.wait_for_successful_login()
        # self.wait.until(EC.presence_of_element_located(self.welcome_message_element))
        # OR
        # self.wait.until(EC.url_contains('/pim/viewEmployeeList'))