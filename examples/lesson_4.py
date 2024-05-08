import time


class Person:
    def __init__(self, name, salary):
        # self.person_name = name
        self.name = name
        self.net_worth = 0
        self.hourly_salary = float(salary)
        self.stuff = list()
    def introduce_self(self):
        print(f'My name is {self.name}')
        # print(f'My name is {self.person_name}')

    def check_net_worth(self):
        print(self.net_worth)
        return self.net_worth

    def buy_something(self,thing):
        item = thing['item']
        price = thing['price']
        if price <= self.net_worth:
            self.stuff.append(item)
            self.net_worth -= price
            print(f"{self.name} bought {item} for ${price}.")
        else:
            print(f"{self.name} does not have enough funds to buy {item}.")

    def sell_something(self,item,price):
        if item in self.stuff:
            self.stuff.remove(item)
            self.net_worth += price
            print(f"{self.name} sold {item} for ${price}.")
        else:
            print(f"{self.name} does not have {item} to sell.")


    def do_work(self,hours):
        for h in range (int(hours)):
            time.sleep(1)
            self.net_worth += self.hourly_salary




person1 = Person("Ramya", salary= 55)
person2 = Person("sri", salary= 75)

person2.introduce_self()
person2.do_work(8)

person1.introduce_self()
person1.do_work(4)


print('person 2: ')
person2.check_net_worth()

print('person 1: ')
person1.check_net_worth()

person1.buy_something({'item': 'toy car', 'price':65.99})
print(person1.stuff)
print(person1.net_worth)

person1.sell_something('toy car',40)
print(person1.stuff)
print('Person 1 net worth:', person1.net_worth)
