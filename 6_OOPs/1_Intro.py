'''
oops
--
class
object
encapsulation
data abstraction
inheritance
polymorphism

class:
---
state:
---
Instance variables
Class Variables

Behaviour:
-----
Instance Methods
Class Methods

'''
class Employee:
    # State
    def __init__(self, id, name, sal):
    # Behaviour
    # id, name, sal -->variables
    # self.id,self.name,self.sal---> instance variables
        self.id = id
        self.name = name
        self.sal = sal
    def get_details_emp(self):
        print("Emp details are:",self.id,self.name,self.sal)
# sarath is an object for Employee
sarath = Employee(101,'vishnu',100000)
sarath.get_details_emp()

