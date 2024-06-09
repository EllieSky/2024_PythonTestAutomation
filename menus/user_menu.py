from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from menus.base_menu import BaseMenu



class UserMenu(BaseMenu):
    usr_menu_msg = (By.ID, 'welcome')

    # def __init__(self, browser):
    #     self.browser = browser
    #     self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)
    def get_greeting(self):
        return self.browser.find_element(*self.usr_menu_msg).text

    def logout(self):
        self.browser.find_element(*self.usr_menu_msg).click()
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()