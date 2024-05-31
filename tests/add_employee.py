import unittest

from fixtures.base_fixture import AdminLoginFixture
from pages import employee_list


class AddEmployee(AdminLoginFixture):
    def test_add_employee_with_credentials(self):
        self.employee_list.add()
#          in the employee list im going to  click the add-add_employee.create_login_details
#          in the add employee page fill in required info
#          on the same page i want to click the login details
#          then after clicking save button we are going to be on personal detail page and then check for the details
#          on the user menu logout
#          self. login page
#          after login check for check for (user,pass)
#          user get message



if __name__ == '__main__':
    unittest.main()
