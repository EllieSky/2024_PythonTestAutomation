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

