
class Person:
    def __init__(self, name, salary):
        # self.person_name = name
        self.name = name
        self.net_worth = 0
        self.hourly_salary = float(salary)
        self.stuff = list()

    def introduce_self(self):
        print(f'My name is {self.name}')

    def check_net_worth(self):
        print(self.net_worth)
        return self.net_worth

    def buy_something(self, thing):
        # add to inventory
        pass

    def sell_something(self, thing):
        # remove from inventory
        pass

    def do_work(self, hours):
        # yes, you can also you multiplication :)
        for h in range(int(hours)):
            self.net_worth += self.hourly_salary


person1 = Person("Mariaa", 55)
person2 = Person("Steve", 50)

person2.introduce_self()
person2.do_work(8)

person1.introduce_self()
person1.do_work(4)

print('person 1: ')
person1.check_net_worth()


print('person 2: ')
person2.check_net_worth()