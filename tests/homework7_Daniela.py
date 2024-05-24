import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture.base_fixture import AdminLoginFixture

class EmployeeSearch(AdminLoginFixture):

    def test_sorting_first_name_column(self):
        browser = self.browser
        browser.get('http://hrm-online.portnov.com/')
        wait = WebDriverWait(browser, 10)

        # Login
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()
        wait.until(EC.visibility_of_element_located((By.ID, 'menu_pim_viewPimModule')))

        # Navigate to the Employee List
        browser.find_element(By.ID, 'menu_pim_viewPimModule').click()
        wait.until(EC.visibility_of_element_located((By.ID, 'resultTable')))

        # Click on First (& Middle) Name column header
        first_name_header_xpath = "//a[contains(text(),'First (& Middle) Name')]"
        wait.until(EC.element_to_be_clickable((By.XPATH, first_name_header_xpath))).click()
        time.sleep(2)

        def get_first_name_list():
            return [name.text.lower() for name in browser.find_elements(By.XPATH, "//table[@id='resultTable']//tr/td[3]")]

        # Validate sorting on the first page
        names = get_first_name_list()
        self.assertTrue(names == sorted(names), "Names are not sorted in ascending alphabetical order")

        # Check if pagination exists and handle it
        while True:
            pagination = browser.find_elements(By.CLASS_NAME, 'paging')
            if pagination:
                try:
                    # Check if 'Next' button is present and clickable
                    next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Next')))
                    next_button.click()
                    time.sleep(2)

                    # Get and validate sorting on the next page
                    new_names = get_first_name_list()
                    self.assertTrue(new_names == sorted(new_names), "Names on the new page are not sorted in ascending alphabetical order")
                    # Ensure the name on the new page continues the order from the last page
                    self.assertTrue(names[-1] <= new_names[0], "Names are not in correct order across pages")
                    names = new_names
                except Exception:
                    # If there is no 'Next' button, break the loop
                    break
            else:
                break

if __name__ == "__main__":
    unittest.main()





