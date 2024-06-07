from pages.base_pages.base_page import BasePage


class BaseEmployeeInfo(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        # implement and add as part of homework:
        # self.employee_info_menu = EmployeeInfoMenu(self.browser)

    def go_to_page(self, employee_code):
        self.browser.get(self.PAGE_URL + employee_code)

    def get_employee_code(self):
        return self.browser.current_url.split('/')[-1]