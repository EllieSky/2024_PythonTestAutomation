import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('https://demoqa.com/login')

    def tearDown(self):
        self.browser.quit()


    def test_1_valid_login(self):
        browser = self.browser
        browser.find_element(By.ID, "userName").send_keys('EllieSky')
        browser.find_element(By.ID, "password").send_keys('Password1!')
        browser.find_element(By.ID, "login").location_once_scrolled_into_view
        browser.find_element(By.ID, "login").click()

        time.sleep(5)  # to give time for actual login process

        self.assertIn('/profile', self.browser.current_url)
        self.assertEqual('elliesky', self.browser.find_element(By.ID, 'userName-value').text)

        btn_logout_txt = browser.find_element(By.ID, 'submit').text
        self.assertEqual('Log out', self.browser.find_element(By.ID, 'submit').text)

    def test_2_invalid_password(self):
        browser = self.browser
        browser.find_element(By.ID, "userName").send_keys('EllieSky')
        browser.find_element(By.ID, "password").send_keys('Password!')
        browser.find_element(By.ID, "login").location_once_scrolled_into_view
        browser.find_element(By.ID, "login").click()

        time.sleep(5)  # to give time for actual login process

        self.assertEqual('Invalid username or password!', self.browser.find_element(By.ID, 'name').text)

    def test_3_no_password(self):
        browser = self.browser
        browser.find_element(By.ID, "userName").send_keys('EllieSky')
        browser.find_element(By.ID, "login").location_once_scrolled_into_view
        browser.find_element(By.ID, "login").click()

        time.sleep(5)  # to give time for actual login process

        class_attr_value = browser.find_element(By.ID, 'password').get_attribute('class')
        self.assertIn('is-invalid', class_attr_value)

    def test_4_no_user_name(self):
        browser = self.browser
        browser.find_element(By.ID, "password").send_keys('Password1!')
        browser.find_element(By.ID, "login").location_once_scrolled_into_view
        browser.find_element(By.ID, "login").click()

        time.sleep(5)  # to give time for actual login process

        class_attr_value = browser.find_element(By.ID, 'userName').get_attribute('class')
        self.assertIn('is-invalid', class_attr_value)


if __name__ == '__main__':
    unittest.main()
