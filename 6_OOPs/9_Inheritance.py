'''
Creating new classes from existing classes, so that new classes will acquire all the features of the
existing classes is called inheritance.

1.Sinle inheritance
2.Multiple inheritance
3.Multi level
4.hirearchical
5.Hybird inheritance

'''

class Teac:
    def setid(self,id):
        self.id = id
    def getid(self):
        return self.id
    def setadd(self,addr):
        self.addr = addr
    def getadd(self):
        return self.addr
t = Teac()
t.setid(101)
t.setadd("kadiri")
print(t.getid())
print(t.getadd())




# simple inheritance
# Super class
class Person(object):
    def __init__(self, name, idnumber):     # name ---> local variables
        self.name = name                    # self.name---> instance variable
        self.idnumber = idnumber
    def display(self):                      # instance method
        print("Emp details:",self.name,self.idnumber)
# Sub class
class Emp(Person):
    def __init__(self, name, idnumber, sal, post):
        self.sal = sal
        self.post = post
        Person.__init__(self,name,idnumber)     # Here calling sub class to super class
    def dis(self):
        print("sub class Emp details",self.name,self.idnumber,self.sal,self.post)
sub = Emp('sarath',12345,234556,'kdr')      # Here creating an object
sub.display()       # this is super class method
sub.dis()           # this is sub class method

