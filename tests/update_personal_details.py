import unittest

from fixtures.base_fixture import AdminLoginFixture


class UpdatePersonalDetails(AdminLoginFixture):
    def test_update_info_and_job(self):
        emp_name = 'Bob Boss'
        middle_name = 'George'
        ssn = '111-11-1111'
        marital_status = 'Single'
        job_title = 'CEO'
        self.employee_list.search_by_employee_name(emp_name)
        self.employee_list.search()
        self.employee_list.view_record(row=1)   #//table//td[3]/a
        self.personal_details.edit()
        self.personal_details.update_info(ssn = ssn, middle_name = middle_name, mar_status = marital_status)
        self.personal_details.save()
        employee_code = self.personal_details.get_employee_code()
        self.job_page.go_to_page(employee_code)
        self.job_page.edit()
        self.job_page.update_info(job_title=job_title)
        self.job_page.save()
        self.user_menu.logout()
        self.login_page.authenticate('bobboss', 'bobboss')
        self.main_menu.goto_MyInfo()
        # # OR
        # self.my_info.go_to_page()
        actual_data = [
            self.my_info.get_middle_name(),
            self.my_info.get_ssn(),
            self.my_info.get_marital_status()
            ]
        self.assertListEqual([middle_name, ssn, marital_status], actual_data)
        self.job_page.go_to_page(employee_code)
        self.assertEqual(job_title, self.job_page.get_job_title())


if __name__ == '__main__':
    unittest.main()
