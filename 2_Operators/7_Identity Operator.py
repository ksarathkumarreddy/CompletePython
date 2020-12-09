x = 22
if(type(x) is int):
    print("true")
else:
    print("false")


x = 66.00
if(type(x) is not str):
    print("true")
else:
    print("false")

a1 = 34
b1 = 34
print(a1 is not b1)

str1 = 'sarath'         # here string is immutable data type that's why both str varabiles pointing same object.
str2 = 'sarath'
print(str1 is str2)

list1 = [1,2,3]         # here list im mutable that's why both are not pointing same object.
list2 = [1,2,3]
print(list1 is list2)

tuple = (1,2,3)
tuple1 = (1,2,3)
print(tuple is tuple1)

dict = {'name':'sarath','age':22,'génder':'male'}
dict1 = {'name':'sarath','age':22,'génder':'male'}
print(dict is dict1)