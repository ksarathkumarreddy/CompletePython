'''
1.compile time errors  : syntactical errors found in the code
2.logical errors        : errors in the logic of the program
3.runtime erros        : PVM can not execute byte code

Exception:
----
An exception is a runtime error which can be handled by the programmer.
Exception handling:
-------------
The purpose of handling errors is to make the program robust.the word robust means strong.


try
except
else
finally

For any exception is base is baseexception..

Some errors:
---
Type error
zerodivision error
Floating point error
overflowerror

All errors are classes in python..

'''
'''
    try:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print("a/b is",a/b)
    except ZeroDivisionError as zd:
        print("please enter other than 0 for b",zd)
    else:
        print("program executed successfully")
    finally:
        print("closing operation")
'''
def get_number(x, y):
    try:
        print("---In try block-----")
        res = x/y
        print("result for divison is:",res)
    except Exception as e:
        print("Based on the value we get an error",e)
    else:
        print("executed")
    finally:
        print("successfully completed")
get_number(22,0)



