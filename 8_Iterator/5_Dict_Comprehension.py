# Dict Comprehension
# Syntax  {key: value for (key, value) in iterable}
# Normal dictionary
keys = ['a','b','ç','d','e']
values = [1,2,3,4,5]
mydict = {k:v for k,v in zip(keys,values)}
print(mydict)

# Dict Comprehension
dict = {x: x**2 for x in [1,2,3,4,5]}
print(dict)

# ------
# Set Comprehension
# Here duplicates are not allowed
set = {1,2,3,4,2,1}
compr = {val for val in set}
print(compr)

