from pages import AddEmployee
from pages import EmployeeList
from pages import JobPage
from pages import LoginPage
from pages import PersonalDetails, MyInfo


class Pages:
    def __init__(self, browser):
        self.login_page = LoginPage(browser)
        self.employee_list = EmployeeList(browser)
        self.add_employee = AddEmployee(browser)
        self.personal_details = PersonalDetails(browser)
        self.my_info = MyInfo(browser)
        self.job_page = JobPage(browser)