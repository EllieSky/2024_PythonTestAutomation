import time
from faker import Faker


class Person:
    def __init__(self):
        data = Faker()
        # self.person_name = name
        self.name = data.first_name()
        self.job = data.job()
        self.net_worth = 0
        self.hourly_salary = float(data.random_int(20, 120))
        self.stuff = list()

    def introduce_self(self):
        print(f'My name is {self.name}')

    def report_net_worth(self):
        print(f"{self.name}'s current net worth is: {self.net_worth}")

    def buy_something(self, thing: dict):
        item = thing['item']
        price = thing['price']
        self.stuff.append(item)
        self.net_worth -= price

    def sell_something(self, thing: dict):
        # remove from inventory
        # increase net worth
        pass

    def do_work(self, hours: int):
        # yes, you can also use multiplication :)
        ## time.sleep(hours)
        ## self.net_worth += self.hourly_salary * hours
        for h in range(int(hours)):
            time.sleep(1)
            self.net_worth += self.hourly_salary



####  Create 2 instances of Person class
person1 = Person()
person2 = Person()

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

person1.buy_something({'item': 'toy car', 'price': 65.99})
print(person1.stuff)
print(person1.net_worth)

pass
