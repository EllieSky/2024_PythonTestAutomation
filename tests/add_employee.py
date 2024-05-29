import unittest

from fixtures.base_fixture import AdminLoginFixture


class AddEmployee(AdminLoginFixture):
    def test_add_employee_with_credentials(self):
        self.employee_list.add()
        # add_employee.enter_employee_info()
        # add_employee.create_login_details()
        # add_employee.save()
        # personal_details.get_first_name()
        # personal_details.get_last_name()
        # personal_details.get_emp_id()
        # user_menu.logout()
        self.login_page.authenticate('user', 'pass')
        # user_menu.get_greeting()






if __name__ == '__main__':
    unittest.main()
