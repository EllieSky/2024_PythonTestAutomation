import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from fixtures.base_fixture import BrowserFixture

class HomeWork9(BrowserFixture):

    def test_OrangeHRM(self):
        self.browser.get('http://hrm-online.portnov.com')
        current_window = self.browser.current_window_handle
        self.wait.until(EC.presence_of_element_located((By.ID, 'logInPanelHeading')))
        self.browser.find_element(By.ID, 'btnJoin').click()

        WebDriverWait(self.browser, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.browser.window_handles if window != current_window][0]
        self.browser.switch_to.window(new_window)

        self.assertEqual("https://www.orangehrm.com/", self.browser.current_url)
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Try it for Free')))
        self.assertTrue(self.browser.find_element(By.LINK_TEXT, 'Try it for Free').is_displayed())

        self.browser.close()
        self.browser.switch_to.window(current_window)

        self.assertEqual(1, len(self.browser.window_handles))
        self.assertEqual(current_window, self.browser.current_window_handle)

if __name__ == '__main__':
    unittest.main()
