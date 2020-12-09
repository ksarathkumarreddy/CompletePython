''''
Function is a self block of code which is used to organise the code.
Function can be called as a section of program that is written once and can be executed when ever
required in the program, thus making code reusability.
Function is a subprogram that works on data and produce output.
'''

def sum(a,b):
    print("Printing within the function",a+b)
    return a+b
def msg():
    print("Hello")
    return
result = sum(10,10)
print("Printing Outside",result)
msg()

# return statement is used to respone to the caller function.

def human(name,age):    # here name and age is parameters
    print("Here details about a person name is",name,"and age is",age)
    #return name,age
human('sarath',24)      # here sarath and 24 is arguments
human('vishnu',23)

def msg():
    print("hello")
msg()


