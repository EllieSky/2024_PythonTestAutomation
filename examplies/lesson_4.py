
class Person:

    def __init__(self, name, salary): # create constructor
        #self.person_name = name
        self.name = name
        self.net_worth = 0
        self.hourly_salary = float(salary)
        self.stuff = list()

    def introduce_self(self):
        print(f"My name is {self.name}")
        # print(f"My name is {self.person_name}")


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
        # yes you can also you multiplication :)
        for h in range(int(hours)):
            self.net_worth += self.hourly_salary



person_1 = Person("Maria", 55)
person_2 = Person("Steve", 50)

person_2.introduce_self()
person_2.do_work(8)
print("person_1")
person_2.check_net_worth()

person_1.introduce_self()
person_1.do_work(8)
person_1.check_net_worth()