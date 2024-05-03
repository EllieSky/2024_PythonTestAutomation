class Person:
    def __init__(self, name, salary):
        self.name = name
        self.net_worth = 0
        self.hourly_salary = salary
        self.stuff = list()

    def introduce_self(self):
        print(f'My name is {self.name}')

    def check_net_worth(self):
        print(self.net_worth)
        return self.net_worth

    def buy_something(self, thing):
        pass

    def sell_something(self, thing):
        pass

    def do_work(self):
        for h in range (int(hours)):
            self.net_worth += self.hourly_salary

person1 = Person("Maria")
person2 = Person("Steve")

person2.introduce_self()
person1.introduce_self()
