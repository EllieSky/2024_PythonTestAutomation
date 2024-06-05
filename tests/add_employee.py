import unittest
from faker import Faker

from fixtures.base_fixture import AdminLoginFixture


class AddEmployee(AdminLoginFixture):

    data = Faker()

    def test_add_employee_with_credentials(self):
        first_name = self.data.first_name()
        last_name = self.data.last_name()

        self.employee_list.add()
        #### same result as :
        #### self.add_employee.go_to_page()

        self.add_employee.enter_employee_info(first_name, last_name)
        self.add_employee.create_login_details(first_name[0]+last_name)
        self.add_employee.save()

        self.assertEqual(first_name, self.personal_details.get_first_name())
        self.assertEqual(last_name, self.personal_details.get_last_name())

        # self.user_menu.logout()
        self.login_page.authenticate(first_name[0]+last_name)
        # self.assertEqual(f"Welcome {first_name.capitalize()}", self.user_menu.get_greeting())
        pass






if __name__ == '__main__':
    unittest.main()