from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import BASE_URL, DEFAULT_PASSWORD
from selenium.webdriver.support import expected_conditions as EC

class AddEmployee(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/addEmployee'

    fld_first_name = (By.ID, 'firstName')
    fld_last_name = (By.ID, 'lastName')
    fld_middle_name = (By.ID, 'middleName')
    fld_employee_id = (By.ID, 'employeeId')
    fld_user_name = (By.ID, 'user_name')
    fld_password = (By.ID, 'user_password')
    fld_re_password = (By.ID, 're_password')
    chk_create_login_details = (By.ID, 'chkLogin')

    btn_save = (By.ID, 'btnSave')

    def enter_employee_info(self, first_name, last_name, middle_name='', employee_id=None):
        self.wait.until(EC.presence_of_element_located(self.fld_first_name)).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located(self.fld_last_name)).send_keys(last_name)
        if middle_name:
            self.wait.until(EC.presence_of_element_located(self.fld_middle_name)).send_keys(middle_name)
        if employee_id is not None:
            self.browser.find_element(*self.fld_employee_id).send_keys(employee_id)
    def create_login_details(self, username, password=DEFAULT_PASSWORD, re_password=DEFAULT_PASSWORD):
        self.wait.until(EC.presence_of_element_located(self.chk_create_login_details)).click()
        self.wait.until(EC.visibility_of_element_located(self.fld_user_name)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.fld_password)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(self.fld_re_password)).send_keys(re_password)
    def save(self):
        self.wait.until(EC.presence_of_element_located(self.btn_save)).click()
