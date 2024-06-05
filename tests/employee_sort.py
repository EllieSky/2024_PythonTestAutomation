import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.base_fixture import AdminLoginFixture


class EmployeeSort(AdminLoginFixture):
    # create a variable and use inspect -> copy -> XPath,  to take a way tag <a>
    # the way is - //*[@id="resultTable"]/thead/tr/th[3]/a and remove thead/tr for make our way short
    first_middle_name_header = (By.XPATH, '//*[@id="resultTable"]//th[3]/a')

    def test_sort_by_first_middle_name(self):
        # ____BASED____
        browser = self.browser
        # without * is a tuple (картеж/список), and * gave us to unpacking the tuple for take a data separate
        browser.find_element(*self.first_middle_name_header).click()
        # time.sleep(2)
        # change time.sleep(2) to self.wait.until(EC.url_contains('sortField=firstMiddleName')),
        # this is important because we won't spend more time than necessary loading the requested page
        self.wait.until(EC.url_contains('sortField=firstMiddleName'))
        # ____EXPERT____
        # create a variable which will find CLASS_NAME paging, it means if the result of it NOTHING the equal will
        # be FALSE, and if result will be SOMETHING the equal will be TRUE
        has_pagination = browser.find_element(By.CLASS_NAME, 'paging')
        # or the same with XPATH - has_pagination = browser.find_element(By.XPATH, '//ul[contains(@class,"paging")]')
        # or the same with CSS_SELECTOR - has_pagination = browser.find_element(By.CSS_SELECTOR, '#frmList_ohrmListComponent>div.top>ul')
        # create variable for while loop, while loop will repeat wile value will be False
        is_last_page = False
        # create a variable for write inside a name for check it for repeating
        previous = ''
        while not is_last_page:
            # XPath way is //*[@id="resultTable"]/tbody/tr[1]/td[3]/a, but we can change * on table, for more offisient
            # this lokator //*[@id="resultTable"]/tbody/tr[1]/td[3]/a - meaning: go to the tbody and finde
            # me 1 role and 3 sell and get link tag out of this sell
            # we remove [1] for get all rolls and change finde_element to finde_elements
            list_of_name_elements = browser.find_elements(By.XPATH, '//table[@id="resultTable"]//tr/td[3]/a')
            # create a loop for check list of names avaliable repeating
            for name_element in list_of_name_elements:
                # checking previous name the same with name_element
                self.assertLessEqual(previous, name_element.text)
                # adn write this name_element to previous
                previous = name_element.text
            # ____ADVANCED____
            # create a loop for list of pagination if it is True, means while site don't list all pages
            if has_pagination:
                # crate a value with text which contain name of pages
                pagination_text = browser.find_element(By.CSS_SELECTOR, '.paging .desc').text
                # make a split of our text with number of pages
                pagination_pieces = pagination_text.split(' of ')
                # check is current page is the equal the last page or not,
                # if is it False the loop while will be repeated, if True, the loop will be completed
                is_last_page = pagination_pieces[-1] in pagination_pieces[0]
                # create a loop for list page if it is current page is not last
                if not is_last_page:
                    # fine element of CSS_SELECTOR .next>a and click it for change to the next page
                    browser.find_element(By.CSS_SELECTOR, '.next>a').click()
            else:
                is_last_page = True
        # # ____EXPERT____
        # # and repeat previous searching
        # list_of_name_elements = browser.find_elements(By.XPATH, '//table[@id="resultTable"]//tr/td[3]/a')
        # for name_element in list_of_name_elements:
        #     self.assertLessEqual(previous, name_element.text)
        #     previous = name_element.text

if __name__ == '__main__':
    unittest.main()
