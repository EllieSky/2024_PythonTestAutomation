import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from fixtures.base_fixture import AdminLoginFixture


class EmployeeSearch(AdminLoginFixture):

    def test_search_by_job_title(self):
        expected_job_title = "QA Manager"

        browser = self.browser
        job_title_select = Select(browser.find_element(By.ID, 'empsearch_job_title'))
        job_title_select.select_by_visible_text(expected_job_title)
        browser.find_element(By.ID, 'searchBtn').click()
        time.sleep(1)

        list_of_records = browser.find_elements(By.CSS_SELECTOR, '#resultTable>tbody td:nth-child(5)')
        for record in list_of_records:
            displayed_job_title = record.text
            self.assertEqual(expected_job_title, displayed_job_title)

        # displayed_job_title = browser.find_element(By.CSS_SELECTOR, '#resultTable>tbody td:nth-child(5)').text
        # self.assertEqual(expected_job_title, displayed_job_title)

        self.assertEqual('QA Manager', browser.find_element(By.XPATH, "//td[text()='QA Manager']").text)


if __name__ == '__main__':
    unittest.main()
