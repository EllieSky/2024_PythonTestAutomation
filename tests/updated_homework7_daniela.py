import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture.base_fixture import AdminLoginFixture

class EmployeeSearch(AdminLoginFixture):

    def test_sorting_first_name_column(self):
        wait = WebDriverWait(self.browser, 10)

        try:
            # Wait for the element with partial link text 'First (& Middle) Name' to be clickable
            element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'First (& Middle) Name')))
            element.click()
        except Exception as e:
            print("Error:", e)
            return

        time.sleep(2)  # Give some time for the page to load

        def get_first_name_list():
            return [name.text.lower() for name in self.browser.find_elements(By.XPATH, "//table[@id='resultTable']//tr/td[3]")]

        names = get_first_name_list()
        self.assertTrue(names == sorted(names), "Names are not sorted in ascending alphabetical order")

        while True:
            pagination = self.browser.find_elements(By.CLASS_NAME, 'paging')
            if pagination:
                next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Next')))
                if next_button:
                    next_button.click()
                    time.sleep(2)

                    new_names = get_first_name_list()
                    self.assertTrue(new_names == sorted(new_names), "Names on the new page are not sorted in ascending alphabetical order")
                    self.assertTrue(names[-1] <= new_names[0], "Names are not in correct order across pages")
                    names = new_names
                else:
                    break
            else:
                break

if __name__ == "__main__":
    unittest.main()


