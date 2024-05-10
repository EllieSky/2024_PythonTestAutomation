import time
import unittest


class Person:
    def __init__(self, name, salary, items=None):
        self.net_worth = 0
        self.name = name
        self.hourly_salary = float(salary)
        self.stuff = items if items else []

    def introduce_self(self):
        return f"My name is {self.name}"

    def check_net_worth(self):
        return self.net_worth

    def buy_something(self, thing):
        item = thing['item']
        price = thing['price']
        if self.net_worth >= price:
            self.stuff.append(item)
            self.net_worth -= price
            return "Purchase successful."
        else:
            return "Not enough funds to buy this item."

    def sell_something(self, thing):
        item = thing['item']
        price = thing['price']
        if item in self.stuff:
            self.stuff.remove(item)
            self.net_worth += price
            return "Sale successful."
        else:
            return "Item not found in possessions."

    def do_work(self, hours):
        self.net_worth += self.hourly_salary * hours

    def show_possessions(self):
        return f"{self.name}'s possessions: {self.stuff}"


class TestPerson(unittest.TestCase):
    def test_buy_something_with_enough_funds(self):
        maria = Person("Maria", 55)
        maria.net_worth = 300  # Manually set net worth for testing
        result = maria.buy_something({'item': 'laptop', 'price': 250})
        self.assertIn('laptop', maria.stuff)
        self.assertEqual(maria.net_worth, 50)
        self.assertEqual(result, "Purchase successful.")

    def test_buy_something_without_enough_funds(self):
        maria = Person("Maria", 55)
        maria.net_worth = 100  # Manually set net worth for testing
        result = maria.buy_something({'item': 'laptop', 'price': 250})
        self.assertNotIn('laptop', maria.stuff)
        self.assertEqual(result, "Not enough funds to buy this item.")
        self.assertEqual(maria.net_worth, 100)

    def test_sell_something_in_possessions(self):
        maria = Person("Maria", 55, ['banana'])
        result = maria.sell_something({'item': 'banana', 'price': 1.50})
        self.assertNotIn('banana', maria.stuff)
        self.assertEqual(maria.net_worth, 1.50)
        self.assertEqual(result, "Sale successful.")

    def test_sell_something_not_in_possessions(self):
        maria = Person("Maria", 55)
        result = maria.sell_something({'item': 'banana', 'price': 1.50})
        self.assertEqual(result, "Item not found in possessions.")
        self.assertEqual(maria.net_worth, 0)


if __name__ == '__main__':
    unittest.main()
