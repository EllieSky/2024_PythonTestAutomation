from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from blocks.base_block import BaseBlock


class SearchClearBlock(BaseBlock):
    btn_search = (By.ID, 'searchBtn')
    btn_reset = (By.ID, 'resetBtn')

    def search(self):
        self.wait.until(EC.presence_of_element_located(self.btn_search)).click()

    def reset(self):
        self.wait.until(EC.presence_of_element_located(self.btn_reset)).click()