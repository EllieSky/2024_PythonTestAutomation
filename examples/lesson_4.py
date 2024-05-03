class Person:
    def __init__(self, name, salary): #contructor
     #   self.person_name = name   #store name into this self container
        self.name = name
        self.net_worth = 0
        self.hourly_salary = float(salary)
        self.stuff = list()
    def introduce_self(self):
        print(f'My name is {self.name}')
     #   print(f'My name is {self.person_name}')

    def check_net_worth(self):
        # print networth
        print(self.net_worth)
        return self.net_worth


    def buy_something(self, thing):
        # add to inventory
        pass

    def sell_something(self, thing):
        # remove to inventory
        pass

    def do_work(self, hours):
        #you can use multiplication
        for h in range(int(hours)):
            self.net_worth += self.hourly_salary


        pass


#create an instance of that class
person1 = Person("Maria", 55) #() invoke contructor method
person2 = Person("Steve", 35)

person2.introduce_self()
person2.do_work(8)
person1.introduce_self()
person1.do_work(4)

print("person 1: ")
person1.check_net_worth()
print("person 2: ")
person2.check_net_worth()