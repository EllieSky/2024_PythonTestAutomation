from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from tests import BASE_URL
class EmployeeList(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/viewEmployeeList'
    btn_add = (By.ID, 'btnAdd')

    def add(self):
        self.wait.until(EC.presence_of_element_located(self.btn_add)).click()
        self.wait.until(EC.url_changes(self.PAGE_URL))
        self.wait.until(EC.url_changes(self.PAGE_URL))

    def search_by_employee_name(self, emp_name):
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint'))
        ).send_keys(emp_name, Keys.ENTER)

    def search(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'searchBtn'))).click()

    def view_record(self, row=1):
        self.browser.find_element(By.XPATH, f'//table//tr[{row}]/td[3]/a').click()