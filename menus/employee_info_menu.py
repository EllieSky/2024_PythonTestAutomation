from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from menus.base_menu import BaseMenu
# from pages.job_page import JobPage
from tests import DEFAULT_WAIT

class EmployeeInfoMenu(BaseMenu):
    job_mi = (By.XPATH, '//ul[@id="sidenav"]//a[text()="Job"]')
    personal_details_mi = (By.XPATH, '//ul[@id="sidenav"]//a[text()="Personal Details"]')
    # def __init__(self, browser):
    #     self.browser = browser
    #     self.wait = WebDriverWait(browser, DEFAULT_WAIT)
    def goto_job(self):
        self.wait.until(EC.presence_of_element_located(self.job_mi)).click()

        # self.wait.until(EC.url_to_be(JobPage(self.browser).PAGE_URL))

    def goto_Personal_Details(self):
        self.wait.until(EC.presence_of_element_located(self.personal_details_mi)).click()

