import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginTestHwk(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('https://demoqa.com/login')

    def tearDown(self):
        self.browser.quit()

    def test_no_password(self):
        browser = self.browser
        browser.find_element(By.ID, 'userName').send_keys('EllieSky')
        browser.execute_script("arguments[0].scrollIntoView();", browser.find_element(By.ID, 'login'))
        browser.find_element(By.ID, 'login').click()

        time.sleep(3)
        self.assertIn('login', browser.current_url)
        user_form_present = browser.find_element(By.ID, 'userForm').is_displayed()
        self.assertTrue(user_form_present, "User form is not present, login might have succeeded unexpectedly.")

        password_field = browser.find_element(By.ID, 'password')
        validation_error = browser.find_element(By.CSS_SELECTOR, 'input#password:invalid')
        self.assertIsNotNone(validation_error, "Password field does not show required validation error.")

if __name__ == '__main__':
    unittest.main()
