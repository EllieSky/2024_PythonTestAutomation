from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from tests import BASE_URL


class PersonalDetails(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/viewEmployee/empNumber/'

    fld_first_name = (By.ID, 'personal_txtEmpFirstName')
    fld_last_name = (By.ID, 'personal_txtEmpLastName')
    fld_employee_id = (By.ID, 'personal_txtEmployeeId')

    def go_to_page(self, employee_code):
        self.browser.get(self.PAGE_URL + employee_code)

    def get_first_name(self):
        return self.wait.until(EC.presence_of_element_located(self.fld_first_name)).get_attribute('value')

    def get_last_name(self):
        return self.wait.until(EC.presence_of_element_located(self.fld_last_name)).get_attribute('value')

    def get_emp_id(self):
        return self.wait.until(EC.presence_of_element_located(self.fld_employee_id)).get_attribute('value')