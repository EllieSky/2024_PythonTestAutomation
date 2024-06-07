import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

# Page Objects
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://hrm-online.portnov.com/symfony/web/index.php/auth/login")

    def login(self, username, password):
        self.driver.find_element(By.ID, "txtUsername").send_keys(username)
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)
        self.driver.find_element(By.ID, "btnLogin").click()

class EmployeePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_add_employee_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "menu_pim_viewPimModule"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnAdd"))
        ).click()

    def add_employee_details(self, first_name, middle_name, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        ).send_keys(first_name)

        self.driver.find_element(By.ID, "middleName").send_keys(middle_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)

    def create_login_details(self, username, password):
        self.driver.find_element(By.ID, "chkLogin").click()
        self.driver.find_element(By.ID, "user_name").send_keys(username)
        self.driver.find_element(By.ID, "user_password").send_keys(password)
        self.driver.find_element(By.ID, "re_password").send_keys(password)

    def save_employee(self):
        self.driver.find_element(By.ID, "btnSave").click()

class TestEmployeeCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.employee_page = EmployeePage(self.driver)
        self.fake = Faker()

    def tearDown(self):
        self.driver.quit()

    def test_employee_creation(self):
        self.login_page.open()
        self.login_page.login("Admin", "password")

        self.employee_page.go_to_add_employee_page()

        first_name = self.fake.first_name()
        middle_name = self.fake.first_name()
        last_name = self.fake.last_name()
        unique_username = self.fake.unique.user_name()
        password = "Password123!"  # You can use Faker to generate this as well if needed

        self.employee_page.add_employee_details(first_name, middle_name, last_name)
        self.employee_page.create_login_details(unique_username, password)
        self.employee_page.save_employee()

        # Verify that the employee was created
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//h1[text()='Personal Details']"))
        )

        # Logout
        self.driver.find_element(By.ID, "welcome").click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
        ).click()

        # Login again with the new credentials
        self.login_page.login(unique_username, password)

        # Verify the login was successful
        welcome_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "welcome"))
        ).text

        self.assertIn(first_name, welcome_message, f"Expected welcome message to contain {first_name}, but got {welcome_message}")

if __name__ == "__main__":
    unittest.main()

