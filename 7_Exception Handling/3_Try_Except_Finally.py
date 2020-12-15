'''
try:
---
If any error occcurs in try block...
Python stop the execution and then go to Except block.
We can handle the exception in Except block.
then if except block also get an error at that time only.
Comes to else block
Then next, finally block will be executed...


'''

def get_number(x,y):
    try:
        print("-----In try block------")
        res = x/y
        print("The result for division is:",res)
        float_res = round(24.601/0.0123,4.6)
    except Exception as err:
        print("please make sure give me positive number only",err)
    else:
        print('---------in else block only------')
    finally:
        print("closing operation")
get_number(20,10)


class AgeInvalidError(object):
    pass


try:
    age = int(input("Enter your age:"))
    print("Age is",age)
    if age>=18:
        print('you are eligible to vote')
    else:
        raise AgeInvalidError("Age must be greater than 18")
except AgeInvalidError as ne:
    print("An exception occured",ne)
finally:
    print("Voting process completed")


