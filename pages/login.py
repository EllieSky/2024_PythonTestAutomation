from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from tests import DEFAULT_WAIT, ADMIN_USER, DEFAULT_PASSWORD, BASE_URL


class LoginPage(BasePage):
    PAGE_URL = f'{BASE_URL}/auth/login'
    page_header = (By.ID, 'logInPanelHeading')

    welcome_message_element = (By.ID, 'welcome')

    def authenticate(self, username=ADMIN_USER, password=DEFAULT_PASSWORD):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys(username)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()

    def wait_for_successful_login(self):
        self.wait.until(EC.presence_of_element_located(self.welcome_message_element))