''''
strings having an immutable nature.
which means we can not modify the data once we create.
Creating as simple as single quotes or double quotes or triple quotes also.
charater data type is not available in python..,,so single character also represent str only.
mutable and immutable nature:
--------
mutable we can modify the content
immutable means we canot modify the content

sequence:
--------
string
list
tuple
bytearrays
buffer
xrange


we can perform all the types of sequence..

adding
multypling
checking for membership
indexing
slicing
finding largest and smallest element
finding length of the sequence.
'''

str = "python programing"   # creating string
print(str)
print(type(str))

print(str[0]) # indexing

print(str[1:5])  # slicing

# updating string

var = "hello world"
print("updating string", var[:6]+"python")




a = 11
b = 11
print(a is b)




li = [1,2,3]
li1 = [1,2,3]
print(li is li1)

di = {1:2,3:4}
di1 = {1:2,3:4}
print(di is di1)


