from math import *

class Employee:
    def __init__(self, name: str, age: int, people: int):
        self.name = name
        self.age = age
        self.people = people

class Manager(Employee):

    def income(self):
        return f'{(log2(self.people) + 1)*1000000 / self.age : .0f}'    
        
class Developer(Employee):

    def income(self):
        return f'{(log2(self.people) + 1)*1000000 / self.age : .0f}' 

man = Manager('Артем', 20, 12)
dev = Developer('Гриша', 18, 1)
print(dev.income(), man.income())
