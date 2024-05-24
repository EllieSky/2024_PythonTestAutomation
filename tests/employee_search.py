import time
import unittest
from selenium.webdriver.common.by import By

class EmployeeSearch(AdminLoginFixture):

    def test_search_by_job_title(self):
        expected_job_title = "QA Manager"

        browser = self.browser
        job_title_select = Select(browser.find_element(By.ID, 'empsearch_job_title'))
        job_title_select.select_by_visible_text(expected_job_title)
        browser.find_element(By.ID, 'searchBtn').click()

            self.assertEqual(expected_job_title, displayed_job_title)


if __name__ == '__main__':
    unittest.main()
