from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    def autenticate(self, username='admin', password='password'):
        self.browser.find_element(By.CSS_SELECTOR, '#txtUsername').send_keys(f'{username}')
        self.browser.find_element(By.CSS_SELECTOR, '#txtPassword').send_keys(f'{password}')
        self.browser.find_element(By.CSS_SELECTOR, '#btnLogin').click()



    def wait_for_login(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#welcome')))
