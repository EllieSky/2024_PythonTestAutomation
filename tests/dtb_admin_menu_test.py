import unittest

from selenium.webdriver.common.by import By

from fixtures.base_fixture import AdminLoginFixture
from menus.dtb_main_menu import MainMenu


class AdminMenu(AdminLoginFixture):
    def test_open_localization_via_menu(self):
        MainMenu(self.browser).goto_Admin_Config_Localization()
        self.assertEqual('Localization', self.browser.find_element(By.ID, 'localizationHeading').text)


if __name__ == '__main__':
    unittest.main()
