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


Constructor:
----
It is a special operator in python.
__init__ is an constructor
It is used to intialize the instance variable and methods.
Its an optinal because default constructor will be there.
In __init__ inside one special constructor will be there which is called __new__.
Where as __new__ can be used to create an object.
__init__ can be intialized to an object.

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

