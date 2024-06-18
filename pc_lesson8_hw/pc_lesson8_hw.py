import time
import unittest

import self
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pc_fixtures.base_fixture import AdminLoginFixture
from pc_pages.pc_login import LoginPage
from selenium.webdriver.support import expected_conditions as EC, wait


class AddUser(AdminLoginFixture):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def test_add_person(self):
        self.wait = WebDriverWait(self.browser, 10)
        person_random = Faker()
        first_name = person_random.first_name()
        last_name = person_random.last_name()
        login_page = LoginPage(self.browser)
        login_page.wait_for_login()
        self.password = person_random.password()
        self.username = first_name + person_random.zipcode()
        self.browser.find_element(By.CSS_SELECTOR, '#btnAdd').click()
        self.browser.find_element(By.CSS_SELECTOR, '#firstName').send_keys(first_name)
        self.browser.find_element(By.CSS_SELECTOR, '#lastName').send_keys(last_name)
        employee_id = self.browser.find_element(By.CSS_SELECTOR, '#employeeId').get_attribute('value')
        self.browser.find_element(By.CSS_SELECTOR, '#chkLogin').click()
        login_page.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#user_name')))
        self.browser.find_element(By.CSS_SELECTOR, '#user_name').send_keys(str(self.username))
        self.browser.find_element(By.CSS_SELECTOR, '#user_password').send_keys(f'{self.password}')
        self.browser.find_element(By.CSS_SELECTOR, '#re_password').send_keys(f'{self.password}')
        self.browser.find_element(By.CSS_SELECTOR, '#btnSave').click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#profile-pic > h1')))

        first_last_name = self.browser.find_element(By.CSS_SELECTOR, '#profile-pic > h1').text

        self.assertEqual(first_last_name, f"{first_name} {last_name}")

        self.browser.find_element(By.CSS_SELECTOR, '#welcome').click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#welcome-menu > ul > li:nth-child(2) > a')))
        self.browser.find_element(By.CSS_SELECTOR, '#welcome-menu > ul > li:nth-child(2) > a').click()

        self.wait.until(EC.url_contains('http://hrm-online.portnov.com/symfony/web/index.php/auth/login'))
        has_login = self.browser.find_element(By.CSS_SELECTOR, '#btnLogin')
        login_exist = False
        if has_login:
            login_exist = True

        self.assertEqual(True, login_exist)
        self.browser.find_element(By.CSS_SELECTOR, '#txtUsername').send_keys(f'{self.username}')
        self.browser.find_element(By.CSS_SELECTOR, '#txtPassword').send_keys(f'{self.password}')
        self.browser.find_element(By.CSS_SELECTOR, '#btnLogin').click()
        self.wait.until(EC.url_contains('viewMyDetails'))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#welcome')))

        created_user = self.browser.find_element(By.CSS_SELECTOR, '#welcome').text
        self.assertEqual(f'Welcome {first_name}', created_user)

        pass


if __name__ == '__main__':
    unittest.main()
