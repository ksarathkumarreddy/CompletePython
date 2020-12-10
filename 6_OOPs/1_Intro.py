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
state
behaviour

'''
class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    def get_details_emp(self):
        print("Emp details are:",self.id,self.name,self.sal)
sarath = Employee(101,'vishnu',100000)
sarath.get_details_emp()
