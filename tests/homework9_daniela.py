from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Step 1: Log in to hrm-online.portnov.com
    driver.get("http://hrm-online.portnov.com")
    username_field = driver.find_element(By.ID, "txtUsername")
    password_field = driver.find_element(By.ID, "txtPassword")
    login_button = driver.find_element(By.ID, "btnLogin")

    username_field.send_keys("admin")
    password_field.send_keys("password")
    login_button.click()

    # Step 2: Click the top-right green button - Join OrangeHRM Community
    join_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Join OrangeHRM Community"))
    )
    join_button.click()

    # Step 3: Switch to the new window
    original_window = driver.current_window_handle
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Step 4: Validate that you were redirected to orangehrm.com site
    WebDriverWait(driver, 10).until(EC.url_contains("orangehrm.com"))

    # Step 5: Handle pop-up and wait for it to disappear
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass

    # # Step 6: Validate that ‘Try it for Free’ button is displayed
    # try_it_free_button = WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//a[text()='Try it for Free']"))
    # )
    # assert try_it_free_button.is_displayed()

    # Step 7: Close the window and return back to the original document
    driver.close()
    driver.switch_to.window(original_window)

    # Step 8: Validate that all other windows are closed and you are in the correct window
    assert len(driver.window_handles) == 1
    assert driver.current_window_handle == original_window

finally:
    driver.quit()

