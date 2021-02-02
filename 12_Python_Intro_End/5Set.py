# set does not support indexing and slicing.
months = {'jan','mar','feb'}
months.add('april')
print(months)

for m in months:
    print(m)

days = set(['mon','wed','fri','tue','thur','sun','sat'])
days.discard('sun')
for d in days:
    print(d)


# union
DaysA=set(["Mon","Tue","Wed"])
DaysB=set(["Wed","Thu","Fri","Sat","Sun"])
AllDays=DaysA|DaysB
print(AllDays)


# By using square of a list
list1 = [1,2,3,4,5]
sq_li = list(map(lambda val : val ** 2, list1))
print(sq_li)

# deque
from collections import deque
queue = deque(['name','age','gender'])
print(queue)
queue.append('surname')
print(queue)
queue.popleft()
print(queue)

from collections import namedtuple
Student = namedtuple('Student',['name','age'])
s = Student('sarath',23)
print(s.name)


from collections import Counter
list = [10,20,10,20,10]
print(Counter(list))






