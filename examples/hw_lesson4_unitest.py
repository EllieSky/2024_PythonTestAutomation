import time
import unittest


class Person:
    def __init__(self,name,salary, initial_stuff):
        self.name = name
        self.net_worth = 0
        self.hourly_salary = float(salary)
        self.stuff = initial_stuff

    def introduce_self(self):
        print(f'My name is {self.name}')

    def report_net_worth(self):
        print(f"{self.name}'s current net worth is: {self.net_worth:.2f}")

    def buy_something(self, thing: dict):
        # def buy_something() to only work when there is enough funds, otherwise it should return without executing the transaction.
        item = thing['item']
        price = thing['price']
        if price <= self.net_worth:
            self.stuff.append(item)
            self.net_worth -= price
        else:
            return

    def sell_something(self, thing: dict):
        # The function should check if a Person's list of stuff contains the item, and sell it if yes, otherwise it should return without executing the transaction.
        item = thing ['item']
        price = thing ['price']
        if item in self.stuff:
            self.stuff.remove(item)
            self.net_worth += price
        else:
            return

    def do_work(self, hours: int):
        for h in range(int(hours)):
            time.sleep(1)
            self.net_worth += self.hourly_salary
class TestPerson (unittest.TestCase):
    def setUp (self):
        self.person1 = Person("Maria", 55, ['book', 'pen', 'bag'])
        self.person2 = Person("Steve", 50, ['notebook', 'pencil', 'hat'])

    def test_buy_something(self):
        self.person1.net_worth = 500.00
        self.person1.buy_something({'item': 'shoes', 'price': 400.99})
        self.assertIn('shoes', self.person1.stuff)
        self.assertEqual(self.person1.net_worth, 500.00-400.99)

        self.person2.net_worth = 10.00
        self.person2.buy_something({'item': 'toy car', 'price': 40.99})
        self.assertNotIn('toy car', self.person2.stuff)
        self.assertEqual(self.person2.net_worth, 10.00)

    def test_sell_something(self):
        self.person1.net_worth = 100.00
        self.person1.sell_something({'item': 'book', 'price': 24.00})
        self.assertNotIn('book', self.person1.stuff)
        self.assertEqual(self.person1.net_worth, 100.00 + 24.00)

        self.person2.net_worth = 50.00
        self.person2.sell_something({'item': 'toy car', 'price': 14.59})
        self.assertNotIn('flower', self.person2.stuff)  # flower was never in stuff
        self.assertEqual(self.person2.net_worth, 50.00)

    def test_do_work(self):
        self.person1.do_work(4)
        self.assertEqual(self.person1.net_worth, 55.00*4)

        self.person1.do_work(8)
        self.assertEqual(self.person2.net_worth, 50.00 * 8)



if __name__ == '__main__':
    unittest.main()
