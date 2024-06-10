import time
import unittest


from faker import Faker
from selenium.webdriver.common.by import By

from pc_fixtures.base_fixture import AdminLoginFixture
from pc_pages.pc_login import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(AdminLoginFixture):
    def test_add_person(self):
        person_random = Faker()
        first_name = person_random.first_name()
        last_name = person_random.last_name()
        login_page = LoginPage(self.browser)
        login_page.wait_for_login()
        self.browser.find_element(By.CSS_SELECTOR, '#btnAdd').click()
        self.browser.find_element(By.CSS_SELECTOR, '#firstName').send_keys(first_name)
        self.browser.find_element(By.CSS_SELECTOR, '#lastName').send_keys(last_name)
        employee_id = self.browser.find_element(By.CSS_SELECTOR, '#employeeId').get_attribute('value')
        self.browser.find_element(By.CSS_SELECTOR, '#chkLogin').click()
        username = (By.CSS_SELECTOR, '#user_name')
        login_page.wait.until(EC.visibility_of_element_located(username))
        self.browser.find_element(By.CSS_SELECTOR, '#user_name').send_keys(str(first_name))
        self.browser.find_element(By.CSS_SELECTOR, '#user_password').send_keys('password')
        self.browser.find_element(By.CSS_SELECTOR, '#re_password').send_keys('password')
        self.browser.find_element(By.CSS_SELECTOR, '#btnSave').click()
        print(employee_id)
        time.sleep(10)






        pass


if __name__ == '__main__':
    unittest.main()
