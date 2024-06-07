from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:
    def __init__(self, driver):
        self.driver = driver

    def add_employee(self, first_name, middle_name, last_name, username, password):
        self.driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "btnAdd"))).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "middleName").send_keys(middle_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "chkLogin").click()
        self.driver.find_element(By.ID, "user_name").send_keys(username)
        self.driver.find_element(By.ID, "user_password").send_keys(password)
        self.driver.find_element(By.ID, "re_password").send_keys(password)
        self.driver.find_element(By.ID, "btnSave").click()

        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Personal Details']"))
        )
