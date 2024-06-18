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


class MyTestCase(AdminLoginFixture):

    def __init__(self, methodName: str = "runTest"):

        super().__init__(methodName)



    def test_add_person(self):
        self.wait = WebDriverWait(self.browser, 10)
        person_random = Faker()
        first_name = person_random.first_name()
        last_name = person_random.last_name()
        login_page = LoginPage(self.browser)
        login_page.wait_for_login()
        password = person_random.password()
        username = first_name + person_random.zipcode()
        print(password)
        print(username)
        self.browser.find_element(By.CSS_SELECTOR, '#btnAdd').click()
        self.browser.find_element(By.CSS_SELECTOR, '#firstName').send_keys(first_name)
        self.browser.find_element(By.CSS_SELECTOR, '#lastName').send_keys(last_name)
        employee_id = self.browser.find_element(By.CSS_SELECTOR, '#employeeId').get_attribute('value')
        self.browser.find_element(By.CSS_SELECTOR, '#chkLogin').click()
        # username = (By.CSS_SELECTOR, '#user_name')
        login_page.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#user_name')))
        self.browser.find_element(By.CSS_SELECTOR, '#user_name').send_keys(str(username))
        self.browser.find_element(By.CSS_SELECTOR, '#user_password').send_keys(f'{password}')
        self.browser.find_element(By.CSS_SELECTOR, '#re_password').send_keys(f'{password}')
        self.browser.find_element(By.CSS_SELECTOR, '#btnSave').click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#profile-pic > h1')))

        first_last_name = self.browser.find_element(By.CSS_SELECTOR, '#profile-pic > h1').text

        self.assertEqual(first_last_name, f"{first_name} {last_name}")

        print(employee_id)
        self.browser.find_element(By.CSS_SELECTOR, '#welcome').click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#welcome-menu > ul > li:nth-child(2) > a')))
        self.browser.find_element(By.CSS_SELECTOR, '#welcome-menu > ul > li:nth-child(2) > a').click()

        self.assertEqual(True, self.browser.find_element(By.CSS_SELECTOR, '#welcome-menu > ul > li:nth-child(2) > a'))

        # select = Select(self.browser.find_element(By.CSS_SELECTOR, '#welcome'))

        # select.select_by_value('logout')
        time.sleep(3)


        pass


if __name__ == '__main__':
    unittest.main()
