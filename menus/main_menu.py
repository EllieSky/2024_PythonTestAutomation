from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MainMenu:

    admin_menu = (By.ID, 'menu_admin_viewAdminModule')
    admin_user_manag_mi = (By.ID, 'menu_admin_UserManagement')
    admin_user_manag_config_mi = (By.ID, 'menu_admin_Configuration')
    admin_user_manag_config_localiz_mi = (By.ID, 'menu_admin_localization')
    admin_user_manag_config_modules_mi = (By.ID, 'menu_admin_viewModules')
    my_info_menu = (By.ID, 'menu_pim_viewMyDetails')


    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)

    def goto_Admin_Config_Localization(self):
        actions = self.actions

        actions.move_to_element(self.browser.find_element(*self.admin_menu))
        actions.move_by_offset(xoffset=0, yoffset=20)
        actions.move_to_element(self.browser.find_element(*self.admin_user_manag_config_mi))
        actions.click(self.browser.find_element(*self.admin_user_manag_config_localiz_mi))

        actions.perform()
        actions.reset_actions()

    def goto_Admin_Config_Modules(self):
        actions = self.actions

        actions.move_to_element(self.browser.find_element(*self.admin_menu))
        actions.move_by_offset(xoffset=0, yoffset=20)
        actions.move_to_element(self.browser.find_element(*self.admin_user_manag_config_mi))
        actions.click(self.browser.find_element(*self.admin_user_manag_config_modules_mi))

        actions.perform()
        actions.reset_actions()
    def goto_MyInfo(self):
        self.browser.find_element(*self.my_info_menu).click()
