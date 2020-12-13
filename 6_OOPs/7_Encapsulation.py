'''
Encapsulation:
-----
Best example is normal calss for encapsulation..
Encapsulation is nothing but writing attributes and methods inside a class.
Methods process the data available in the variables.
Hence data and code are bundle up together in the class.

'''
class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    def get_student_details(self):
        print("Student details are:",self.id, self.name, self.age)
sarath = Student(101,'vishnu',23)       # Here sarath is a refference variable for an object
sarath.get_student_details()


