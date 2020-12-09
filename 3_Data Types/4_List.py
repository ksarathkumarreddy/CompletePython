''''
list is a most versatile data type available in python which can be written as a list of comma separated
values in the square brackets.
list contain both homogenius data and heterogenuos data.

items in the list need not to be the same ..
list is mutable.
mutable means we can modify the data..

In mutable we can perform CRUD Operations
duplicates are allowed in list.


If we want to represent group of individual objects as a single entity where insertion order preserved ,
duplicate objects are allowed,heterogenus objects are also aloowed,then we should go for list.
List is a dynamic nature we can increase the size and decrease the size.
In list the elements will be placed within square brackets and with comma separator.
we can differentiate duplicate elements by using index and we can preserve insertion order by using index.
index will play a important role.
'''

list = ['physics','science',1,2,3,4]
print(list)

list1 = [11,12,13,14]
print(list1)

print(list[0])
list[0]='sarath'
print(list)

del list
print(list)

# Here we can perform CRUD operations

# Create
list = [1,2,'sarath']
print(list)
# Retrieve
print(list[2])
# Update
list[2] = 'vishnu'
print(list)
# Delete
del list
print(list)


