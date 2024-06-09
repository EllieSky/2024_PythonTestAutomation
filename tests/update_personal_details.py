import unittest

from fixtures.base_fixture import AdminLoginFixture


class UpdatePersonalDetails(AdminLoginFixture):
    def test_update_info_and_job(self):
        emp_name = 'Bob Boss'
        middle_name = 'George'
        ssn = '111-11-1111'
        marital_status = 'Single'
        job_title = 'CEO'
        self.page.employee_list.search_by_employee_name(emp_name)
        self.page.employee_list.search()
        self.page.employee_list.view_record(row=1)
        self.page.personal_details.edit()
        self.page.personal_details.update_info(middle_name = middle_name, ssn = ssn, mar_status = marital_status)
        self.page.personal_details.save()
        employee_code = self.page.personal_details.get_employee_code()
        self.page.job_page.go_to_page(employee_code)
        self.page.job_page.edit()
        self.page.job_page.update_info(job_title=job_title)
        self.page.job_page.save()

        self.user_menu.logout()
        self.page.login_page.authenticate('bobboss', 'bobboss')
        self.main_menu.goto_MyInfo()
#         or
#       self.my_info.go_to_page()
        actual_data = [
            self.page.my_info.get_middle_name(),
            self.page.my_info.get_ssn(),
            self.page.my_info.get_marital_status()
            ]
        self.assertListEqual([middle_name, ssn, marital_status],actual_data)
        self.page.job_page.employee_info_menu.goto_job()
        self.assertEqual(job_title, self.page.job_page.get_job_title())

if __name__ == '__main__':
    unittest.main()
