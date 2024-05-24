import unittest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fixtures.base_fixture import AdminLoginFixture


class AddingEmployee(AdminLoginFixture):
    welcome_message_element = (By.ID, 'welcome')
    def test_add_new_employee(self):
        fake = Faker()
        browser = self.browser

        first_name = fake.first_name()
        last_name = fake.last_name()
        username = fake.user_name()
        self.wait = WebDriverWait(browser, 10)
        browser.find_element(By.XPATH, '//input[@id="btnAdd"]').click()
        self.wait.until(EC.url_contains('pim/addEmployee'))
        browser.find_element(By.XPATH, '//input[@id="firstName"]').send_keys(first_name)
        browser.find_element(By.XPATH, '//input[@id="lastName"]').send_keys(last_name)
        browser.find_element(By.XPATH, '//input[@id="chkLogin"]').click()
        element1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="user_name"]')))
        element1.send_keys(username)
        element2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="user_password"]')))
        element2.send_keys('password')
        element3 = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="re_password"]')))
        element3.send_keys('password')
        browser.find_element(By.XPATH, '//input[@id="btnSave"]')
        self.wait = WebDriverWait(browser, 10)
        # self.wait.until(EC.url_contains())
        # self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="personal_txtEmpFirstName"]')))

        first_name_displayed = browser.find_element(By.XPATH, '//input[@id="personal_txtEmpFirstName"]').get_attribute('value')
        last_name_displayed = browser.find_element(By.XPATH, '//input[@id="personal_txtEmpLastName"]').get_attribute('value')
        # employee_id = browser.find_element(By.XPATH, '//input[@id="personal_txtEmployeeId"]').get_attribute('value')
        self.assertEqual(first_name_displayed, first_name)
        self.assertEqual(last_name_displayed, last_name)
        browser.find_element(By.CSS_SELECTOR, '//*[@id="welcome-menu"]/ul/li[2]/a').click()
        self.wait.until(EC.url_contains('/index.php/auth/login'))
        browser.find_element(By.CSS_SELECTOR, '//*[@id="divUsername"]/span').send_keys(username)
        browser.find_element(By.CSS_SELECTOR, '//*[@id="divPassword"]/span').send_keys('password')
        browser.find_element(By.XPATH, '//input[@id="btnLogin"]')
        self.wait.until(EC.presence_of_element_located(self.welcome_message_element))


if __name__ == '__main__':
    unittest.main()
