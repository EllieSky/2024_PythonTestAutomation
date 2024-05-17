import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fixture.base_fixture import AdminLoginFixture

class EmployeeSearch(AdminLoginFixture):

    def test_search_by_job_title(self):
        expected_job_title = "QA Manager"

        browser = self.browser
        browser.get('http://hrm-online.portnov.com/')
        time.sleep(2)

        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()
        time.sleep(2)  # Wait for login to complete

        welcome_message = browser.find_element(By.ID, 'welcome').text
        self.assertIn('Welcome', welcome_message)

        job_title_select = Select(browser.find_element(By.ID, 'empsearch_job_title'))
        job_title_select.select_by_visible_text(expected_job_title)
        browser.find_element(By.ID, 'searchBtn').click()
        time.sleep(2)

        list_of_records = browser.find_elements(By.CSS_SELECTOR, '#resultTable>tbody>tr')

        # Advanced:
        for row in list_of_records:
            displayed_job_title = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
            self.assertEqual(expected_job_title, displayed_job_title)


if __name__ == '__main__':
    unittest.main()
