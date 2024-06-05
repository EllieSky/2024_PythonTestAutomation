from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from tests import BASE_URL


class PersonalDetails(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/viewEmployee/empNumber/'

    fld_first_name = (By.ID, 'personal_txtEmpFirstName')
    fld_last_name = (By.ID, 'personal_txtEmpLastName')
    fld_employee_id = (By.ID, 'personal_txtEmployeeId')

    btn_save = (By.ID, 'btnSave')
    btn_edit = btn_save

    def __init__(self, browser):
        super().__init__(browser)
        self.fld_nick_name = (By.ID, 'personal_txtEmpNickName')
        self.select_marital_status = (By.ID, 'personal_cmbMarital')
        self.fld_middle_name = (By.ID, 'personal_txtEmpMiddleName')
        self.fld_ssn = (By.ID, 'personal_txtNICNo')

    def go_to_page(self, employee_code):
        self.browser.get(self.PAGE_URL + employee_code)

    def get_employee_code(self):
        return self.browser.current_url.split('/')[-1]

    def get_first_name(self):
        return self.wait.until(EC.presence_of_element_located(self.fld_first_name)).get_attribute('value')

    def get_last_name(self):
        return self.wait.until(EC.presence_of_element_located(self.fld_last_name)).get_attribute('value')

    def get_emp_id(self):
        return self.wait.until(EC.presence_of_element_located(self.fld_employee_id)).get_attribute('value')

    def get_middle_name(self):
        return self.wait.until(EC.presence_of_element_located(self.fld_middle_name)).get_attribute('value')

    def get_ssn(self):
        return self.wait.until(EC.presence_of_element_located(self.fld_ssn)).get_attribute('value')

    def get_marital_status(self):
        return Select(self.browser.find_element(*self.select_marital_status)).first_selected_option.text

    def edit(self):
        self.wait.until(EC.presence_of_element_located(self.btn_edit)).click()
        self.wait.until(EC.element_to_be_clickable(self.fld_first_name))

    def update_info(self, middle_name = None, ssn = None, mar_status = None, nick_name = None):
        if ssn is not None:
            self.browser.find_element(*self.fld_ssn).clear()
            self.browser.find_element(*self.fld_ssn).send_keys(ssn)

        if middle_name is not None:
            self.browser.find_element(*self.fld_middle_name).clear()
            self.browser.find_element(*self.fld_middle_name).send_keys(middle_name)

        if mar_status is not None:
            Select(self.browser.find_element(*self.select_marital_status)
                   ).select_by_visible_text(mar_status)
            
        if nick_name is not None:
            self.browser.find_element(*self.fld_nick_name).clear()
            self.browser.find_element(*self.fld_nick_name).send_keys(nick_name)

    def save(self):
        self.wait.until(EC.presence_of_element_located(self.btn_save)).click()
        self.wait.until_not(EC.element_to_be_clickable(self.fld_first_name))


class MyInfo(PersonalDetails):
    PAGE_URL = f'{BASE_URL}/pim/viewMyDetails'