from pages.base_pages.base_employee_info import BaseEmployeeInfo
from pages.base_pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from tests import BASE_URL


class JobPage(BaseEmployeeInfo):
    @property
    def PAGE_URL(self):
        return f'{BASE_URL}/pim/viewJobDetails/empNumber/'

    btn_save = (By.ID, 'btnSave')
    btn_edit = btn_save

    def __init__(self, browser):
        super().__init__(browser)
        self.select_emp_status = (By.ID, 'job_emp_status')
        self.select_job_title = (By.ID, 'job_job_title')

    def get_job_title(self):
        return Select(self.browser.find_element(*self.select_job_title)).first_selected_option.text

    def edit(self):
        self.wait.until(EC.presence_of_element_located(self.btn_edit)).click()
        self.wait.until(EC.element_to_be_clickable(self.select_job_title))

    def update_info(self, job_title=None, emp_status=None):
        if job_title is not None:
            Select(self.browser.find_element(*self.select_job_title)
                   ).select_by_visible_text(job_title)

        if emp_status is not None:
            Select(self.browser.find_element(*self.select_emp_status)
                   ).select_by_visible_text(emp_status)

    def save(self):
        self.wait.until(EC.presence_of_element_located(self.btn_save)).click()
        self.wait.until_not(EC.element_to_be_clickable(self.select_job_title))

