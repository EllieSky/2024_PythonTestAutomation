import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class AdminLoginFixture(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')
        self.browser.find_element(By.CSS_SELECTOR, '#txtUsername').send_keys('admin')
        self.browser.find_element(By.CSS_SELECTOR, '#txtPassword').send_keys('password')
        self.browser.find_element(By.CSS_SELECTOR, '#btnLogin').click()

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
