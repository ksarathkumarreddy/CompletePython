c = 10 # it's not good
count = 10 # it makes some sense
emp_id = 101
print(emp_id)
# single variable having multiple values
eid = 101,102,104,'sarath'
print(eid)
# multiple variables having multiple values
id, name, age = 101, 'sarath', 24
print(id,name,age)

# Local variables
'''
A variable declared inside the function's body is know as a local variables.
'''
def msg():
    name = 'sarath'

msg()
print(name)

def emp(age):
    y = 'bharath'
    print(y)
  #  age = int(input("enter age"))
    if age>22:
        print("all are eligible")
    else:
        print('not eligible')

emp(age)
# Global variables
'''
A variables declared outside the function body and inside function also declared is know as global variables.
'''

sarath_age = 24
def sarath():
    global sarath_age
    print("sarath age local",sarath_age)
sarath()
print('sarath age global',sarath_age)

