import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SearchUsingGoogle(unittest.TestCase):
    def test_google_hello(self):
        str_input = 'hello'

        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://www.google.com')
        browser.find_element(By.NAME, 'q').send_keys(str_input, Keys.RETURN)

        page_title = browser.title
        self.assertEqual(f'{str_input} - Google Search', page_title)

        page_url = browser.current_url
        self.assertIn(f'/search?q={str_input}', page_url)

        top_link_text = browser.find_element(By.CSS_SELECTOR, '[role="link"] [role="heading"]').text
        self.assertEqual(str_input.capitalize(), top_link_text)


if __name__ == '__main__':
    unittest.main()
