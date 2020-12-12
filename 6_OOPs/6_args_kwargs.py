'''
*args(Non-Keyword arguments)
**kwargs(Keyword arguments)

arg:
---
In Python, we can pass a variable number of arguments to a function using special symbols.

Note:
--
“We use *args and **kwargs as an argument when we have no doubt about
the number of  arguments we should pass in a function.”

'''

# *args
def myfun(*argv):
    for arg in argv:
        print(arg)
myfun("hello ","sarath")

# example
def myfun1(arg1,*argv):
    print("First argument",arg1)
    for arg in argv:
        print("next arg through *argv",arg)
myfun1('hello','welcome','sarath')



# ** kwargs

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

    # Driver code


myFun(first='Geeks', mid='for', last='Geeks')  