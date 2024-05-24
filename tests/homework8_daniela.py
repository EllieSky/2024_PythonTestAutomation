import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate fake data
first_name = fake.first_name()
middle_name = fake.first_name()
last_name = fake.last_name()
unique_username = fake.unique.user_name()
password = "Password123!"  # You can use Faker to generate this as well if needed

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # 1. Open the login page
    driver.get("http://hrm-online.portnov.com/symfony/web/index.php/auth/login")

    # Login
    driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("password")  # Change to your actual password
    driver.find_element(By.ID, "btnLogin").click()

    # Wait for the PIM page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "menu_pim_viewPimModule"))
    )

    # 2. Go to Employee Information page
    driver.find_element(By.ID, "menu_pim_viewPimModule").click()

    # Click the 'Add' button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnAdd"))
    ).click()

    # 3. Wait for the Add Employee page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    # Fill out required fields
    driver.find_element(By.ID, "firstName").send_keys(first_name)
    driver.find_element(By.ID, "middleName").send_keys(middle_name)
    driver.find_element(By.ID, "lastName").send_keys(last_name)

    # 4. Select Create Login Details check-box
    driver.find_element(By.ID, "chkLogin").click()

    # Fill out username and password fields
    driver.find_element(By.ID, "user_name").send_keys(unique_username)
    driver.find_element(By.ID, "user_password").send_keys(password)
    driver.find_element(By.ID, "re_password").send_keys(password)

    # 5. Save the new employee
    driver.find_element(By.ID, "btnSave").click()

    # 6. Verify that the employee was created
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//h1[text()='Personal Details']"))
    )

    # Logout
    driver.find_element(By.ID, "welcome").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    ).click()

    # 7. Login again with the new credentials
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txtUsername"))
    )
    driver.find_element(By.ID, "txtUsername").send_keys(unique_username)
    driver.find_element(By.ID, "txtPassword").send_keys(password)
    driver.find_element(By.ID, "btnLogin").click()

    # 8. Verify the login was successful and the welcome message contains the correct name
    welcome_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "welcome"))
    ).text

    assert first_name in welcome_message, f"Expected welcome message to contain {first_name}, but got {welcome_message}"

finally:

    driver.quit()
