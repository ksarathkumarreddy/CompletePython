'''
Iterator:
---------
Iterator in python is an object that is used to iterate over iterable objcts like list,
tuple,dict and set.
1.iter() to intialization of an iterator.
2.next() next value of iterator.
3.End of iteration raises stopiteration at end of signal..

## When we require faster iteration,irrespective of memory constraints we will go for iterator.

python 2.x:
-----
range(iterator)----> Memory will be allocated for all values
xrange(Generator)---> Memory will be allocated for one value at a time it's take time to much..

python 3.x:
-------
range---> Generator


'''

class FibIterable:
    def __init__(self, iLast=1, iSecondLast=1,iMax=500):
        self.iLast = iLast
        self.iSecondLast = iSecondLast
        self.iMax = iMax
    def __iter__(self): # To intialize
        return self
    def __next__(self):
        iNext = self.iLast + self.iSecondLast
        if iNext > self.iMax:
            raise StopIteration()
        self.iSecondLast = self.iLast
        self.iLast = iNext
        return iNext
myobj = FibIterable()
for val in myobj:
    print(val)



iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)

while True:
    try:

        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        # exception will happen when iteration will over
        break



