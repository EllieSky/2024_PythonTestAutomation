import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture.base_fixture import AdminLoginFixture


class EmployeeSearch(AdminLoginFixture):

    wait = None
    driver = webdriver

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://hrm-online.portnov.com/')
        cls.wait = WebDriverWait(cls.driver, 10)

        cls.driver.find_element(By.ID, 'txtUsername').send_keys('admin')
        cls.driver.find_element(By.ID, 'txtPassword').send_keys('password')
        cls.driver.find_element(By.ID, 'btnLogin').click()
        cls.wait.until(EC.visibility_of_element_located((By.ID, 'menu_pim_viewPimModule')))

        cls.driver.find_element(By.ID, 'menu_pim_viewPimModule').click()
        cls.wait.until(EC.visibility_of_element_located((By.ID, 'resultTable')))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def get_first_name_list(self):
        return [name.text.strip().lower() for name in
                self.driver.find_elements(By.XPATH, "//table[@id='resultTable']//tr/td[3]")]

    def test_sorting_first_name_column(self):
        driver = self.driver
        wait = self.wait

        first_name_header_xpath = "//a[contains(text(),'First (& Middle) Name')]"
        wait.until(EC.element_to_be_clickable((By.XPATH, first_name_header_xpath))).click()
        time.sleep(2)

        names = self.get_first_name_list()
        self.assertEqual(names, sorted(names), "Names are not sorted in ascending alphabetical order")

        while True:
            pagination = driver.find_elements(By.CLASS_NAME, 'paging')
            if pagination:
                next_button = EC.element_to_be_clickable((By.LINK_TEXT, 'Next'))
                if next_button(wait):
                    next_button(wait).click()
                    time.sleep(2)

                    new_names = self.get_first_name_list()
                    self.assertEqual(new_names, sorted(new_names),
                                     "Names on the new page are not sorted in ascending alphabetical order")
                    self.assertGreaterEqual(new_names[0], names[-1], "Names are not in correct order across pages")
                    names = new_names
                else:
                    break
            else:
                break


if __name__ == "__main__":
    unittest.main()





