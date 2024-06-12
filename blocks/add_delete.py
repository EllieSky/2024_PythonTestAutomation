from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from blocks.base_block import BaseBlock


class AddBlock(BaseBlock):
    PAGE_URL = None
    btn_add = (By.ID, 'btnAdd')

    def add(self):
        self.wait.until(EC.presence_of_element_located(self.btn_add)).click()
        self.wait.until(EC.url_changes(self.PAGE_URL))


class DeleteBlock(BaseBlock):
    btn_delete = (By.ID, 'btnDelete')
    modal_delete = (By.ID), 'deleteConfModal'
    modal_delete_ok = (By.ID, 'dialogDeleteBtn')
    modal_delete_cancel = (By.CSS_SELECTOR, '.btn.cancel')

    def delete(self, ok=True):
        self.wait.until(EC.presence_of_element_located(self.btn_delete)).click()
        self.wait.until(EC.visibility_of_element_located(self.modal_delete))
        if ok:
            self.browser.find_element(*self.modal_delete_ok).click()
        else:
            self.browser.find_element(*self.modal_delete_cancel).click()
        self.wait.until(EC.invisibility_of_element_located(self.modal_delete))


class AddDeleteBlock(AddBlock, DeleteBlock):
    pass
