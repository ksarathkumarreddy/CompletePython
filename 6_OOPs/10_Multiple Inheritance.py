'''
Multiple Inheritance:
--------------
Deriving sub clases from multiple base classes is called multiple inheritance.

MRO Principle:
----
Three things follow MRO Principle:
1.To search for the sub class before going to base class.
2.When a class is inherited from several classes, it search in the order from left to rightin base classes.
3.It will not visit any class more than once.
'''

class Base1(object):
    def __init__(self):
        self.str1 = 'sarath'
        print("base 1")
class Base2(object):
    def __init__(self):
        self.str2 = 'vishnu'
        print("base 2")
class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def printstr(self):
        print(self.str1,self.str2)
obj = Derived()
obj.printstr()


class First_Stu(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name
class Se_Stu(object):
    def __init__(self,age):
        self.age = age
class Students(First_Stu,Se_Stu):
    def __init__(self,id,name,age,gender):
        self.gender = gender
        First_Stu.__init__(self,id,name)
        Se_Stu.__init__(self,age)
    def dis(self):
        print("Student details are:",self.id,self.name,self.age,self.gender)
sarath = Students(103,'vishnu',23,'female')
sarath.dis()
