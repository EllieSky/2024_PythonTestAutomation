from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from blocks.add_delete import AddDeleteBlock
from blocks.results_table import ResultTableBlock
from blocks.search_reset import SearchResetBlock
from pages.base_pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from tests import BASE_URL


class EmployeeList(BasePage, ResultTableBlock, AddDeleteBlock, SearchResetBlock):
    def PAGE_URL(self):
        return f'{BASE_URL}/pim/viewEmployeeList'

    def search_by_employee_name(self, emp_name):
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint'))
        ).send_keys(emp_name, Keys.ENTER)