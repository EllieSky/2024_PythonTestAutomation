import unittest
from io import StringIO
from unittest.mock import patch

from pcherkas_hw_lesson4 import Person


class MyTestCase(unittest.TestCase):
    def test_create_person(self):
        person1 = Person("Petro", 200)
        name = person1.name
        salary = person1.hourly_salary
        expected_name = "Petro"
        expected_hourly_salary = 200
        self.assertEqual(expected_name, name)
        self.assertEqual(expected_hourly_salary, salary)

    def test_introduce(self):
        person1 = Person("Petro", 250)
        name = person1.name
        actual_message = f"My name is {name}"
        expected = "My name is noPetro"
        self.assertEqual(expected, actual_message)

    def test_get_init_networth(self):
        person = Person("Petro", 250)
        init_net_wort = person.net_worth
        expected_net_worth = 0
        self.assertEqual(expected_net_worth, init_net_wort)

    def test_buy_stuff(self):
        person = Person("Petro", 50)
        person.do_work(8)
        person.buy_something({"item": "car", "price": 100})
        expected_item = "car"
        actual_item = person.stuff[-1]
        actual_networth = person.net_worth
        expected_net_worth = 300
        self.assertEqual(expected_item, actual_item)
        self.assertEqual(expected_net_worth, actual_networth)

    def test_sell_stuff(self):
        person = Person("Petro", 50)
        person.do_work(8)
        person.buy_something({"item": "car", "price": 100})
        person.sell_something({"item": "car", "price": 1000})
        actual = len(person.stuff)
        expected = 1
        expected_networth = 1300
        actual_networth = person.net_worth
        self.assertEqual(expected_networth, actual_networth)
        self.assertNotEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
