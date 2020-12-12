#  Normal class having instance variables and instance methods
'''
For ex,
Let us consider, Employee class.
Employee class having   Emp id  Emp name    Emp Sal     Emp Office Adreess(Class variable)
                            I       I           I               Common for every one(sharable data)

Instance variable:
----------
value of a variable is varied from object to object,then such type of variable are called instance variable.
We can declare instance variable:
----------
1.inside constructor
2.inside instance method
3.outside of a class by using reference variable.

'''
class Emp:
    def __init__(self,id, name,sal, office):
        self.id = id                       # id--> local variable
        self.name = name                    # self.id--> instance variable
        self.sal = sal
        self.office = office
    def get_emp_details(self):              # instance method
        print("Emp details are:",self.id, self.name, self.sal, self.office)
vis = Emp(101,'sarath',233333,'blr')
vis.get_emp_details()

'''
Disadvantage of the above code:
---
we are sharing common(sharable) data __init__ method 
which causes memory waste...make it as a class variable..

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