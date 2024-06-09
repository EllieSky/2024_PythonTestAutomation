import time


class Person:

    def __init__(self, name, salary):
        self.name = name
        self.net_worth = 0
        self.hourly_salary = float(salary)
        self.stuff = list()

    def introduce_self(self):
        print(f"My name is {self.name}")

    def check_net_worth(self):
        # print(number*number)
        print(f"your net worth {self.net_worth}")
        return self.net_worth
        pass

    def buy_something(self, thing):
        item = thing["item"]
        price = thing["price"]
        self.stuff.append(item)
        self.net_worth -=price
        pass

    def sell_something(self, thing):
        #remove from inventory
        pass

    def do_work(self, hours):
        #earn money
        for h in range (int(hours)):
            time.sleep(1)
            self.net_worth += self.hourly_salary
        pass

person1 = Person("Petro", 55)
person1.introduce_self()
person1.do_work(4)
person2 = Person("Steve", 50)
person2.introduce_self()
person2.do_work(8)


person1.check_net_worth()

person2.check_net_worth()

person2.buy_something({"item": "toy car", "price": 65.99})
person2.buy_something({"item": "car", "price": 00.99})
person2.check_net_worth()
print(person2.stuff)
