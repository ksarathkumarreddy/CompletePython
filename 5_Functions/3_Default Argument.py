'''
default values to the parameters passed in the function definition, in case value is not
provided then it will take default value.

'''

def msg(id,name,age=23):
    print(id)
    print(name)
    print(age)
msg(101,'sarath',22)

