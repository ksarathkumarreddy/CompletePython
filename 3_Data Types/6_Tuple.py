'''
Tuple is a sequence of immutable objects.
Tuples are sequences, just like list.
Difference between list and tuple are, tuple cannot be changed unlike list and tuple uses paranthesis,
whereas list use square brackets.
Creating a tuple is as simple as putting diferent comma separated values.

'''
# 3 ways to create tuple
tuple = ('sarath','amma',1996,1980)
print(tuple)
print(type(tuple))


tup = 'a','sarath'
print(tup)
print(type(tup))

ex = 1,
print(ex)
print(type(ex))

# create a tuple
tuple1 = ('physics','maths',2000,2001)
print(tuple1)
# retrieving
print(tuple1[0])
print(tuple1[2])

# update
tup = (12,22,223)
tup1 = ('sarath','kumar','redddy')
tup2 = tup + tup1
print(tup2)

# delete
del tup

tup1 = ('sarath','kumar','redddy')
print(sorted(tup1))

