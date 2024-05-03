class Person:

    def __init__(self, person_name, salary):
        self.name = person_name
        self.net_worth = 0
        self.hourly_rate = float(salary)
        self.stuff = list()

    def introduce_self(self):
        print(f'My name is {self.name}.\n')
        # print(f'My name is {self.person_name}.\n')

    def do_math(self):
        # print(number1 * number2)
        pass

    def check_net_worth(self):
        print(f'My net worth is only {self.net_worth}.\n')
        return self.net_worth

    def buy_something(self, thing):
        pass
        # add to inventory

    def sell_something(self, thing):
        pass
        # remove from inventory

    def do_work(self, hours):
        # self.net_worth += self.hourly_rate * hours
        for h in range(int(hours)):
            self.net_worth += self.hourly_rate


person1 = Person('Maria', 55)
person2 = Person('Steve', 50)

person2.introduce_self()
person2.do_work(8)

person1.introduce_self()
person2.do_work(4)

print(f'{person1.name}: ')
person1.check_net_worth()


print(f'{person2.name}: ')
person2.check_net_worth()
