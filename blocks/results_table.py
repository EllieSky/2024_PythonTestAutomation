from selenium.webdriver.common.by import By

from blocks.base_block import BaseBlock


class ResultTableBlock(BaseBlock):
    def sort_by_column(self, column):
        if type(column) == int:
            self.browser.find_element(By.XPATH, f'(//table[@id="resultTable"]//th/a)[{column}]').click()
        else:
            self.browser.find_element(By.XPATH, f'//table[@id="resultTable"]//th/a[text()={str(column)}]').click()

    def view_record(self, row:int=1):
        self.browser.find_element(By.XPATH, f'//table/tbody/tr[{row}]/td[3]/a').click()

    def get_row_data(self, row:int=1):
        data =  [ x.text for x in self.browser.find_elements(By.XPATH, f'//table/tbody/tr[{row}]/td') ]
        data.pop(0)
        return data
