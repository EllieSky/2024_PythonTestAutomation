import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class AdminLoginFixture(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')

    def tearDown(self):
        self.browser.quit()


    def test_search_by_job_title(self):
        expected_job_title = "QA Manager"

        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()
        time.sleep(2)

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

if __name__ == '__main__':
    unittest.main()