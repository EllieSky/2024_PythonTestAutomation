import unittest

from fixtures.base_fixture import AdminLoginFixture


class SystemUsers(AdminLoginFixture):
    def test_system_users_sort(self):
        # self.main_menu.goto_Admin()
        self.page.system_users.go_to_page()
        self.page.system_users.sort_by_column(1)
        self.page.system_users.sort_by_column(1)

        self.page.system_users.search_by_username('bobboss')
        self.page.system_users.search()
        data = self.page.system_users.get_row_data(1)
        self.assertIn('bobboss', data)

if __name__ == '__main__':
    unittest.main()
