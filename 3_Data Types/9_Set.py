'''
Mathematically a set is a collection of items not in any particular order.
elements in the set cannot be duplicates.
maintains no order.
elements in the set are immutable but the set as a whole is mutable.
no indeing in set data type.

'''

days = set(['mon','tue','wed','thu','fri','sat','sun'])
print(days)
days.discard('mon')
print(days)


dates ={12,13,14}
print(dates)

# union
days = set(['mon','tue','wed','thu','fri','sat','sun'])
days1 = set(['mon','tue','fr'])
all = days|days1
print(all)


# intersection
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)


DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)
