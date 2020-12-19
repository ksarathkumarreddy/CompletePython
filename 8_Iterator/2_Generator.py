'''
Generator:
-------
python 2.x:
----
range--->iterator
xrange-->generator

python 3.x:
-----
range---> generator

Generator:
---
1.A generator is a function that returns an object which we can iterate over one value at a time.
2. If a function contains atleat one yield statement, it becomes a generator function..
3. Difference between return and yield is..,
return statement terminates a function entierly..,
yield statement pauses the function saving all its states and later continue from
there on successive calls.


'''
# Iterator mechanism
numbers = [1,2,3,4]
list1 = []
for val in numbers:
    list1.append(val * val)
print("Iterator is:",list1)

# Generator mechanism
numbers = [1,2,3,4]
print("Generator mechanism is:",[val*val for val in numbers])



#Genreator Expr:
x1 = [1,2,3,4]
print("-----------")
lazy_square=(x1*x1 for x1 in numbers)
print(lazy_square)
print(next(lazy_square))
print(list(lazy_square))


