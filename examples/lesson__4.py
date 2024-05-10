import time
from faker import Faker

class Person:
    def __init__(self, name, salary):
        data = Faker()
        self.name = data.first_name()
        self.net_worth = 0
        self.hourly_salary = float(salary)
        self.stuff = list()

    def introduce_self(self):
        print(f'My name is {self.name}')

    def check_net_worth(self):
        print(self.net_worth)
        return self.net_worth

    def buy_something(self, thing):
        item = thing['item']
        price = thing ['price']
        self.stuff.append(item)
        self.net_worth = self.net_worth - price
        pass

    def sell_something(self, thing):
        pass

    def do_work (self, hours):
        for h in range (int(hours)):
            time.sleep(1)
            self.net_worth += self.hourly_salary


person1 = Person("Maria", 55)
person2 = Person("Steve", 50)

person1.introduce_self()
person1.do_work(4)

print('person 1: ')
person1.check_net_worth()

person2.introduce_self()
person2.do_work(8)

print('person 2: ')
person2.check_net_worth()

person1.buy_something({"item": 'toy car', 'price': 65.99})
print(person1.stuff)
print(person1.net_worth)
# d
pass
