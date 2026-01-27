import time
from faker import Faker
import random


class Person():
    def __init__(self, initial_worth = 0):
        data = Faker()
        self.name = data.name()
        self.hourly_salary = float(data.random_int(15,131))
        self.stuff = []
        self.net_worth = initial_worth
        self.hours = data.random_int(1,10)
        self.categories = ["iPhone", "Samsung", "Car", "Book", "Table"]


    def introduce_self(self):
        print(f'Hello, my name is {self.name}')

    def do_work(self):
        for h in range (self.hours):
            time.sleep(0.5)
            self.net_worth += self.hourly_salary

    def check_net_worth(self):
        print(f'My net worth is {self.net_worth}')

    def buy_stuff(self):
        data = Faker()
        things = random.choice(self.categories)
        price =float(data.random_int(1,500))
        new_item = things
        if price <= self.net_worth:
            self.net_worth -= price
            self.stuff.append(new_item)
            print(f'My net worth is {self.net_worth} , because I just bought {new_item} , which costs me {price}')
            print(f'I have this much {self.stuff}')
        else:
             print(f'This {new_item} price {price} is too expensive for me, I\'ll think about buying it one more time')

    def sell_stuff(self):
        data = Faker()
        item = random.choice(self.categories)
        sell_price = float(data.random_int(30,1000))

        if item in self.stuff:
            self.stuff.pop()
            self.net_worth += sell_price
            print(f'My net worth is {self.net_worth}, because i just sold this {item} by this price {sell_price}')
            print(f'I have this much {self.stuff}')
        else:
            print(f'I cannot sell this {item} because I do not own it')




person1 = Person()
person2 = Person()
person3 = Person()
person1.introduce_self()
person1.do_work()
person1.check_net_worth()
person1.buy_stuff()
person1.check_net_worth()
person1.sell_stuff()
person1.sell_stuff()

person2.introduce_self()
person2.do_work()
person2.check_net_worth()
person2.buy_stuff()
person2.sell_stuff()
person2.sell_stuff()
