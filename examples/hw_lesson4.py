import time

class Person:
    def __init__(self, name, salary, initial_stuff):
        self.name = name
        self.net_worth = 0
        self.hourly_salary = float(salary)
        self.stuff = initial_stuff

    def introduce_self(self):
        print(f'My name is {self.name}')

    def report_net_worth(self):
        print(f"{self.name}'s current net worth is: {self.net_worth}")

    def buy_something(self, thing: dict):  # def buy_something() to only work when there is enough funds, otherwise it should return without executing the transaction.
        item = thing['item']
        price = thing['price']
        if price <= self.net_worth:
            self.stuff.append(item)
            self.net_worth -= price
        else:
            return

    def sell_something(self, thing1: dict):
        # The function should check if a Person's list of stuff contains the item, and sell it if yes, otherwise it should return without executing the transaction.
        item1 = thing1 ['item1']
        price1 = thing1 ['price1']
        if thing1 in self.stuff:
            self.stuff.remove(item1)
            self.net_worth += price1
        else:
            return

    def do_work(self, hours: int):
        # yes, you can also use multiplication :)
        ## time.sleep(hours)
        ## self.net_worth += self.hourly_salary * hours
        for h in range(int(hours)):
            time.sleep(1)
            self.net_worth += self.hourly_salary



####  Create 2 instances of Person class
person1 = Person("Maria", 55, ['book', 'pen', 'bag'])
person2 = Person("Steve", 50, ['notebook', 'pencil', 'hat'])

####  Interact with one of the objects
person2.introduce_self()
person2.do_work(8)
print('person 2: ')
person2.report_net_worth()

####  Interact with the other object
person1.introduce_self()
person1.do_work(4)
print('person 1: ')
person1.report_net_worth()

person1.buy_something({'item': 'shoes', 'price': 400.99})
print("Maria's stuff ", person1.stuff)
print("Maria's net_worth ", person1.net_worth)

person2.buy_something({'item': 'toy car', 'price': 40.99})
print("Steve's stuff ", person2.stuff)
print("Steve's net_worth ", person2.net_worth)

person1.sell_something({'item1': 'book', 'price1': 24.00})
print("Maria's stuff ", person1.stuff)
print("Maria's net_worth ", person1.net_worth)

person2.sell_something({'item1': 'hat', 'price1': 14.59})
print("Steve's stuff ", person2.stuff)
print("Steve's net_worth ", person2.net_worth)


