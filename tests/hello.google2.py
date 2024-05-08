import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def test_something(self):
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        browser.get('http://www.google.com')
        browser.find_element(By.NAME, 'q').send_keys('hello', Keys.RETURN)

        page_title = browser.title
        self.assertEqual('hello - Google search', page_title)

        page_url = browser.current_url
        self.assertIn('search?q=hello', page_url)


        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
