import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from fixtures.base_fixture import AdminLoginFixture


class InterviewTestCase(AdminLoginFixture):

    def test_search(self):
        browser = self.browser

        job_title = "QA Manager"
        job_status = "Full Time"

        browser.find_element(By.XPATH, f"//option[text()='{job_title}']").click()
        browser.find_element(By.XPATH, f"//option[text()='{job_status}']").click()

        browser.find_element(By.CSS_SELECTOR, "#searchBtn").click()

        self.wait.until(expected_conditions.element_located_to_be_selected((By.XPATH, f"//select[@id='empsearch_job_title']/option[text()='{job_title}']")))

        # Adding assertion for the result list for QA Manager with a Part Time Employment Status using the for loop.

        job_title_list = browser.find_elements(By.XPATH, f'//*[@id="resultTable"]/tbody/tr/td[5]')
        job_status_list = browser.find_elements(By.XPATH, f'//*[@id="resultTable"]/tbody/tr/td[6]')

        for qa_manager in job_title_list:
            # if job_title == qa_manager.text:
                self.assertEqual(job_title, qa_manager.text)

        for full_time in job_status_list:
            self.assertEqual(job_status, full_time.text)

        url = self.browser.current_url

        browser.find_element(By.ID, "welcome").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Logout']"))).click()
        # browser.find_element(By.XPATH, "//a[text()='Logout']").click()
        self.wait.until(expected_conditions.url_changes(url))
        self.assertIn("/index.php/auth/login", browser.current_url)