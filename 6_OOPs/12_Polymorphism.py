'''
Polymorphism means having many forms.In programming, polymorphism means same function name being uses
for different ways.
1.Operator Overloading
2.Method Overloading
3.Method Overriding

'''

'''
Operator overloading:
---------
when an operator is a symbol that performs some action.
For ex, + is an operator that performs addition operation when used on numbers.
When an operator can perform different actions, it is said to exhibit polymorphism..

'''

print(10+10+22)

s1 = 'sarath'
s2 = 'vishnu'
print(s1+s2)


# Method overloading
'''
Python does't support method overloading.But there are different ways to achieve method overloading inpython.
Problem with method overloading is that may overload the methods and it will take latest defined method only.

If a method is written such that it can perform more than one task.
'''


def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)
product(5,5,5)

# method overriding
'''
When there is a method in the super class, writing the same method in the sub class so that it replaces
the super class method is called method overriding.


'''


class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)

    # Defining child class


class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)

    # Driver's code


obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()