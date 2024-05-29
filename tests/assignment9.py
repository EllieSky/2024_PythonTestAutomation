import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base_fixture import AdminLoginFixture


class HrmAndCommunity(AdminLoginFixture):
    def test_with_windows(self):
        browser = self.browser


        wait = WebDriverWait(browser, 10)
        hrm_button = browser.find_element(By.XPATH, '//*[@id="branding"]/a[1]').text
        self.assertEqual('Join OrangeHRM Community', hrm_button)
        browser.find_element(By.XPATH, '//*[@id="branding"]/a[1]').click()
        # this one htake the current browser in to originalwindow
        original_window = browser.current_window_handle

        # This will wait until the new window is open & the original window is passe in the list
        wait.until(EC.new_window_is_opened([original_window]))
        # in this -1 refers to the last/recent page opened
        new_window_handle = browser.window_handles[-1]
        browser.switch_to.window(new_window_handle)
        wait.until(EC.url_contains('orangehrm.com'))
        current_url = browser.current_url
        self.assertEqual(current_url, 'https://www.orangehrm.com/')
        try_it_free_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Form_submitForm_action_request"]')))
        self.assertEqual(try_it_free_button.get_attribute('value'), '30-Day Free Trial')

        browser.close()
        browser.switch_to.window(original_window)

        self.assertEqual(len(browser.window_handles), 1)



if __name__ == '__main__':
    unittest.main()
