import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.base_fixture import BrowserFixture


class WindowsAndFrames(BrowserFixture):
    def test_with_windows(self):
        self.browser.get('https://demoqa.com/browser-windows')

        current_handles = self.browser.window_handles
        self.browser.find_element(By.ID, 'tabButton').click()
        self.wait.until(EC.new_window_is_opened(current_handles))
        self.browser.switch_to.window(self.browser.window_handles[-1])
        self.assertEqual('This is a sample page', self.browser.find_element(By.ID, 'sampleHeading').text)

        self.browser.switch_to.window(current_handles[0])
        self.assertEqual('DEMOQA', self.browser.title)

        window_btn = self.browser.find_element(By.ID, 'windowButton')
        window_btn.location_once_scrolled_into_view
        window_btn.click()

        self.wait.until(EC.number_of_windows_to_be(3))
        self.browser.switch_to.window(self.browser.window_handles[-1])
        self.assertEqual('This is a sample page', self.browser.find_element(By.ID, 'sampleHeading').text)

        self.browser.close()
        current_handles = self.browser.window_handles
        self.assertEqual(2, len(current_handles))


        pass




if __name__ == '__main__':
    unittest.main()
