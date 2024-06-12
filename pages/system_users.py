from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from blocks.add_delete import AddDeleteBlock
from blocks.results_table import ResultTableBlock
from blocks.search_reset import SearchResetBlock
from pages.base_pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from tests import BASE_URL


class SystemUsers(BasePage, ResultTableBlock, SearchResetBlock, AddDeleteBlock):
    PAGE_URL = f'{BASE_URL}/admin/viewSystemUsers'

    fld_username = (By.ID, 'searchSystemUser_userName')

    def search_by_username(self, username):
        self.wait.until(EC.presence_of_element_located(
            self.fld_username)
        ).send_keys(username, Keys.ENTER)