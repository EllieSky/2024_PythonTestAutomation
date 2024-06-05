import unittest
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.base_fixture import AdminLoginFixture


class EmployeeAdd(AdminLoginFixture):
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']
    random_first_name = random.choice(first_names)
    random_last_name = random.choice(last_names)
    random_user_name = random_first_name + '' + random_last_name
    # add_btn = (By.XPATH, '//input[@id="btnAdd"]')
    # input_name = (By.XPATH, '//input[@id="firstName"]')
    # login_details = (By.XPATH, '//input[@id="chkLogin"]')
    def test_add_employee(self):
        browser = self.browser
        first_name = self.random_first_name
        last_name = self.random_last_name
        user_name = self.random_user_name
        browser.find_element(By.XPATH, '//input[@id="btnAdd"]').click()
        self.wait.until(EC.url_contains('addEmployee'))
        browser.find_element(By.ID, 'firstName').send_keys(first_name)
        browser.find_element(By.ID, 'lastName').send_keys(last_name)
        # change Employee id
        # browser.find_element(By.XPATH, '//input[@id="employeeId"]').send_keys('1111111')

        browser.find_element(By.XPATH, '//input[@id="chkLogin"]').click()
        # username should be every test unic
        browser.find_element(By.XPATH, '//input[@id="user_name"]').send_keys(user_name)
        browser.find_element(By.XPATH, '//input[@id="user_password"]').send_keys('Password')
        browser.find_element(By.XPATH, '//input[@id="re_password"]').send_keys('Password')
        browser.find_element(By.ID, 'btnSave').click()
        # check userName and userLastName in card of created user
        self.assertEqual(first_name, browser.find_element(By.XPATH, '//*[@id="personal_txtEmpFirstName"]').text)
        # // *[ @ id = "personal_txtEmpFirstName"]
        self.assertEqual(last_name, browser.find_element(By.XPATH, '//input[@id="personal_txtEmpLastName"]').text)
        browser.find_element(By.XPATH, '//a[contains(text(),"Logout")]').click()

        # wait
        self.wait.until(EC.url_contains('sortField=firstMiddleName'))


if __name__ == '__main__':
    unittest.main()
