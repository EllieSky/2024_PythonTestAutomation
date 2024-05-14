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

    def test_valid_login(self):
        browser = self.browser
        browser.find_element(By.ID, 'userName').send_keys('EllieSky')
        browser.find_element(By.ID, 'password').send_keys('Password1!')
        browser.find_element(By.ID, 'login').location_once_scrolled_into_view
        browser.find_element(By.ID, 'login').click()

        # After login in, we want to check the expected username is displayed
        self.assertEqual('elliesky', browser.find_element(By.ID, 'userName-value').text)

        self.assertIn('/profile', browser.current_url)

        btn_logout_txt = browser.find_element(By.ID, 'submit').text
        self.assertEqual('Log out', btn_logout_txt)



    def test_invalid_password(self):
        pass

    def test_no_password(self):
        pass


if __name__ == '__main__':
    unittest.main()
