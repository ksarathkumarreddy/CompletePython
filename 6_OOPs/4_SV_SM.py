'''
Static variables can't access instance method and class method.
Any static method can be assigned by @ static method only..
'''

class Employee:
    @staticmethod
    def get_e_data(a,b):
        print("I am in static method",a+b)
Employee.get_e_data(10,10)

'''
IV IM   YES
CV CM   YES
CV IM   YES
IV CM   NO
'''

class Student(object):
    st_school_add = 'kadiri'    # class variables
    unifrom = 'white and black'
    def __init__(self,id,name,age):      # id--> Local variables
        self.id = id                    # self.id---> Instance variables
        self.name = name
        self.age = age
    def get_sarath_details(self):
        print("Sarath details are:",self.id,self.name,self.age)     # normal instance variables
        print("Sarath details are:", self.id, self.name, self.age,self.st_school_add) # here using class variable

    @classmethod
    def everyone(cls):
        print("Common for everyone both school address and uniform:", cls.st_school_add, cls.unifrom)
        #Instance variable cannot access in class method
       # print("Common for everyone both school address and uniform:", cls.st_school_add, cls.unifrom,cls.id)
    @staticmethod
    def get_per_color(color):
        print("Sarath color is:", color)


Student.get_per_color('white')
Student.everyone()
sarath = Student(101,'sarat',24)
sarath.get_sarath_details()