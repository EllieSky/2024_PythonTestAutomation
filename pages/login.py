from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# we created LoginPage for import it in our next test codes
class LoginPage:
    welcome_message_element = (By.ID, 'welcome')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def authenticate(self, username='admin', password='password'):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys(username)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()

    def wait_for_successful_login(self):
        self.wait.until(EC.presence_of_element_located(self.welcome_message_element))