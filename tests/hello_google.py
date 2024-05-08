import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SearchUsingGoogle(unittest.TestCase):
    def test_google_hello(self):
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://www.google.com')
        browser.find_element(By.NAME, 'q').send_keys('hello', Keys.RETURN)

        page_title = browser.title
        self.assertEqual('hello - Google Search', page_title)

        page_url = browser.current_url
        self.assertIn('/search?q=hello', page_url)

        top_link = browser.find_element(By.CSS_SELECTOR, '[role = "link"] [role = "heading"]')
        self.assertEqual('Hello', top_link)


if __name__ == '__main__':
    unittest.main()