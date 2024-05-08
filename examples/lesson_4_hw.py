import unittest
from lesson_4 import Person


class TestBuySell(unittest.TestCase):
    def setUp(self):
        self.person = Person("Test Person", salary=100)

    def test_buy_something(self):
        self.person.buy_something({'item': 'test item', 'price': 40})
        self.assertIn('test item', self.person.stuff)
        self.assertEqual(self.person.net_worth, 40)

    def test_sell_something(self):
        self.person.stuff.append('test item')
        self.person.net_worth = 50
        self.person.sell_something('test item', 30)
        self.assertNotIn('test item', self.person.stuff)
        self.assertEqual(self.person.net_worth, 80)

    def test_sell_nonexistent_item(self):
        self.person.net_worth = 50
        self.person.sell_something('nonexistent item', 30)
        self.assertNotIn('nonexistent item', self.person.stuff)
        self.assertEqual(self.person.net_worth, 50)





class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
