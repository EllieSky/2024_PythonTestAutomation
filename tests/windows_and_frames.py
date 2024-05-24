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

    def test_with_frames(self):
        self.browser.get('https://demoqa.com/nestedframes')
        page_header = self.browser.find_element(By.CSS_SELECTOR, '#framesWrapper>h1').text
        self.assertEqual('Nested Frames', page_header)

        self.browser.switch_to.frame(self.browser.find_element(By.ID, 'frame1'))
        self.assertEqual('Parent frame', self.browser.find_element(By.TAG_NAME, 'body').text)

        self.browser.switch_to.frame(self.browser.find_element(By.TAG_NAME, 'iframe'))
        self.assertEqual('Child Iframe', self.browser.find_element(By.TAG_NAME, 'p').text)

        self.browser.switch_to.default_content()
        page_header = self.browser.find_element(By.CSS_SELECTOR, '#framesWrapper>h1').text
        self.assertEqual('Nested Frames', page_header)


if __name__ == '__main__':
    unittest.main()
