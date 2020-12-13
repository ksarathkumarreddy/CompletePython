'''
Abstract method:
------------
1.A class which contains one or more abstract methods is called an abstract class.
2.An abstract method is a method that has a declaration but does not have an implementation.

'''

from abc import ABC, abstractmethod


class Polygon(ABC):

    # abstract method
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


R = Triangle()
R.noofsides()

R = Pentagon()
R.noofsides()



# Interface
'''
In object-oriented languages like Python, the interface is a collection of method signatures
that should be provided by the implementing class.
Implementing an interface is a way of writing an organized code and achieve abstraction.

'''
