list = ['sarath',11,['bharath','amma']]
print(list)
print(list[2][0])

# 1 Append                  Add element in the last
list = ['sarath','bharath']
list.append("sravs")
print(list)

# 2 Clear
li = [{1,2},('a'),['1.1',2.2]]
li.clear()
print(li)

# 3 Count
vowles = ['a','e','i','o','u','a']
print(vowles.count('a'))

# 4 Extend
names = ['sarath','bharath']
names1 = ['sravs']
names.extend(names1)
print(names)

# 5 Index
vowles = ['a','e','i','o','u','a']
print(vowles.index('i'))

# 6 Insert
vowles = ['a','e','i','u',]
vowles.insert(3,'o')
print(vowles)

# 7 Pop             remove the last element
languages = ['python','java','data science','machine learning']
languages.pop(2)
print(languages)

# 8 Remove          it takes single element and remove the element from the list
animals = ['elephant','dog','fox']
animals.remove('fox')
print(animals)

# 9 Reverse
os = ['windows','linux','mac os']
os.reverse()
print(os)

# 10 Sort               here ascending order or descending order
numbers = [2,3,5,4,1]
numbers.sort()
print(numbers)

# 11 Copy
old_list = [1,2,3]
new_list = old_list
new_list.append('a')
print(old_list)
print(new_list)
