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

        page_title = browser.title

        page_url = browser.current_url



if __name__ == '__main__':
    unittest.main()