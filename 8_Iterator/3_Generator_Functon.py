'''
Generator function returns generator object.
A generator is a function that returns an object which we can iterate over one value at a time.
diff b/w return and yield is...
return statements terminates a function entirely..
yield statement pauses the function saving all its states and later continus from there on
successive calls..

'''

def simple():
    yield 1
    yield 'sarath'
    yield 'bharath'
x = simple()
print(x.__next__())
print(x.__next__())
print(x.__next__())
    
