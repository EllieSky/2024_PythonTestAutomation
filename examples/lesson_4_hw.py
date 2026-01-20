

class Person():
    def __init__(self, name, salary):
        self.net_worth = 0
        self.name = name
        self.hourly_salary = float(salary)
        self.stuff = list()


    def introduce_self(self):
        print(f'My name is {self.name}')

    def do_work(self, hours):
        for h in range (hours):
            self.net_worth += self.hourly_salary

    def check_net_worth(self):
        print(self.net_worth)

    def buy_stuff(self, thing):
        item = thing['item']
        price = thing ['price']

        if self.net_worth >= price:
            self.stuff.append(item)
            self.net_worth -= price
            print(f'I just bought a {item}, which cost me {float(price)}. I have this stuff now {self.stuff}')
            print(f'I have {self.net_worth} money left')
        else:
            print('I don\'t have enough money')


    def sell_stuff(self):
        pass

person1 = Person("Maria", 60)

person1.introduce_self()
person1.do_work(8)
person1.check_net_worth()
person1.buy_stuff ({'item': 'book', 'price' : 555})




