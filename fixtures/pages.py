from pages.add_employee import AddEmployee
from pages.employee_list import EmployeeList
from pages.job_page import JobPage
from pages.login import LoginPage
from pages.personal_details import PersonalDetails, MyInfo


class Pages:
    def __init__(self, browser):
        self.login_page = LoginPage(browser)
        self.employee_list = EmployeeList(browser)
        self.add_employee = AddEmployee(browser)
        self.personal_details = PersonalDetails(browser)
        self.my_info = MyInfo(browser)
        self.job_page = JobPage(browser)