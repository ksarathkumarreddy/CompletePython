class Emp:
    def __init__(self,id, name,sal, office):
        self.id = id
        self.name = name
        self.sal = sal
        self.office = office
    def get_emp_details(self):
        print("Emp details are:",self.id, self.name, self.sal, self.office)
vis = Emp(101,'sarath',233333,'blr')
vis.get_emp_details()

'''
Disadvantage of the above code:
---
we are sharing common(sharable) data __init__ method 
which causes memory waste...mkae it as a class variable..

Firstly,instance variable can use in side constructor only..
where as class variables can sharable and modifiy able...

'''


class Employee:
    office = 'bangalore'
    def __init__(self,id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    # instance method
    def get_emp_details(self):
        print("Emp details are:",self.id, self.name, self.sal,self.office)
    @ classmethod
    def get_class_data(cls):
        print("Employee class shareable data:",cls.office)
Employee.get_class_data()
sarath = Employee(101,'vishnu',23000)
sarath.get_emp_details()
Employee.get_emp_details(sarath)   # it will convert internally like this

'''
class variables:
------
when class is loaded by interpreter and memory allocation will be done at loading itself

Instance variables:
---
When we create an object for class, these will get initialized.

'''