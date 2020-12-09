''''
argument passed in the function call is matched with the function definition on the
basis of the name of the parameter.
'''

def sarath(id,sal):
    print(id)
    print(sal)
sarath(sal=100000,id=10001)
sarath(id=1001,sal=1000000)



# lambda function
squ = lambda x : x * x
print('square of a number is',squ(5))