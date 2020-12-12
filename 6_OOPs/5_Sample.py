'''
We have two methods which are:
1.setter method
2.Getter method
'''
class Emp:
    def __init__(self,id,name,age,sal):
        self.id = id
        self.name = name
        self.age = age
        self.sal = sal
    def get_details(self):
        print("Emp details are",self.id,self.name,self.age,self.sal)
# object related functions C R U D Operations setter, getter
sarath = Emp(101,'sarath',23,23443)
sarath.get_details()
print("Does jeevan has salary",hasattr(sarath,'sal'))   # retrieve
print("Get name of person is",getattr(sarath,'name'))