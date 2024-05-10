import unittest
import time
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

    def test_valid_login(self):
        # eazy for writing
        browser = self.browser
        # found a fill and field user name
        browser.find_element(By.ID, 'userName').send_keys('URus')
        # found fill and field password
        browser.find_element(By.ID, 'password').send_keys('Password1!')
        # scroll if our button covered som windows if this is nes
        browser.find_element(By.ID, 'login').location_once_scrolled_into_view
        # found a button and click it
        browser.find_element(By.ID, 'login').click()
        browser.find_element(By.ID, 'login').get_attribute()
        # never use it. is it solucion for take a paus
        time.sleep(3)
        # check what your user name and loged in user name the same
        self.assertEqual('URus', browser.find_element(By.ID, 'userName-value').text)

        self.assertIn('/profile', browser.current_url)

        btn_logout_txt = browser.find_element(By.ID, 'submit').text
        self.assertEqual('Log out', btn_logout_txt)
        pass


    def test_invalid_password(self):
        pass

    def test_no_password(self):
        browser = self.browser
        browser.find_element(By.ID, 'login').location_once_scrolled_into_view
        browser.find_element(By.ID, 'login').click()

        class_attr_value = browser.find_element(By.ID, 'userName').get_attribute('class')
        self.assertIn('is-invalid', class_attr_value)
        pass
# browser.find_element(By.ID, 'password').get_attribute('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})$')
# ^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})$


if __name__ == '__main__':
    unittest.main()
