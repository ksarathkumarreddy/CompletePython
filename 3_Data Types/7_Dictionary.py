'''
Dictionary is an unordered set of key and value pair. It is a container that contains data,
enclosed within curly braces.
The pair i.e,key and value is known as item...key must be unique.
Each key and value is separeted by colon..,,items as separeted by comma,different items are enclosed in
dictionary.
keys must be of an immutable where as numbers, strings,tuple.
values of a dictionary can be of any type.

where as whole dictionary is mutable.

'''
# creating
dict = {101:"sarath",102:'vishnu'}
print(dict)
print(type(dict))

data = {}
data['rollnum'] = 101
data['name'] = 'tanush'
print(data)

# updating
print(data['name'])
data['profession'] = 'student'
print(data)

# deleting 3 ways
# particular key will be deleted
del data['name']
print(data)

# clear
data.clear()
print(data)

del data

