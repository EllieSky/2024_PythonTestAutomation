import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class AdminLoginFixture(unittest.TestCase):
    def setUp(self, username='admin', password='password'):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')
        self.browser.find_element(By.CSS_SELECTOR, '#txtUsername').send_keys(f'{username}')
        self.browser.find_element(By.CSS_SELECTOR, '#txtPassword').send_keys(f'{password}')
        self.browser.find_element(By.CSS_SELECTOR, '#btnLogin').click()
        self.wait = WebDriverWait(self.browser, 5)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#welcome')))

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
