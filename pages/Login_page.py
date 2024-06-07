from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "txtUsername").send_keys(username)
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)
        self.driver.find_element(By.ID, "btnLogin").click()

        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "menu_pim_viewPimModule"))
        )
