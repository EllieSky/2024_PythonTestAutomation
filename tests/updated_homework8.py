import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from fixture.base_fixture import AdminLoginFixture

class TestEmployeeCreation(AdminLoginFixture):

    def setUp(self):
        super().setUp()
        self.driver = self.get_driver()
        self.wait = WebDriverWait(self.driver, 10)
        self.fake = Faker()

    def tearDown(self):
        self.driver.quit()
        super().tearDown()

    def test_employee_creation_and_login(self):
        self.driver.find_element_by_id("username").send_keys("Admin")
        self.driver.find_element_by_id("password").send_keys("Password")
        self.driver.find_element_by_id("login_button").click()

        add_button = self.wait.until(EC.element_to_be_clickable((By.ID, "add_button")))
        add_button.click()

        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        self.driver.find_element_by_id("first_name").send_keys(first_name)
        self.driver.find_element_by_id("last_name").send_keys(last_name)

        create_login_checkbox = self.driver.find_element_by_id("create_login_checkbox")
        create_login_checkbox.click()

        username = self.fake.user_name() + "_" + self.fake.word()
        password = self.fake.password()

        self.driver.find_element_by_id("username_field").send_keys(username)
        self.driver.find_element_by_id("password_field").send_keys(password)

        self.driver.find_element_by_id("save_button").click()

        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{first_name} {last_name}')]"))))

        self.driver.find_element_by_id("logout_button").click()

        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login_button").click()

        welcome_message = self.wait.until(EC.visibility_of_element_located((By.ID, "welcome_message")))
        self.assertIn(f"Welcome, {first_name} {last_name}", welcome_message.text)

    def get_driver(self):
        # Example: Initialize Chrome WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Maximize browser window
        driver = webdriver.Chrome(options=options)
        return driver

    def setUp(self):
        super().setUp()  # Make sure to call setUp() from the base class
        self.driver = self.get_driver()
        self.wait = WebDriverWait(self.driver, 10)
        self.fake = Faker()


if __name__ == "__main__":
    unittest.main()



