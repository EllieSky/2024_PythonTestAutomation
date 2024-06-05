import unittest

from pc_fixtures.base_fixture import AdminLoginFixture


class MyTestCase(AdminLoginFixture):
    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
