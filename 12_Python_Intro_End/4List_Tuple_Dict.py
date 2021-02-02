
# Creating a list
list = ["sarath",1,2,3,4]
print(list)

# Retreving a list
print(list[0])

# Updating a list
list[0] = 'vishnu'
print(list)

# Deleting a list
del list[1]
print(list)

# List methods
# Append     Add the element at the last
name_list = ['sarath','bharath','amma']
name_list.append('nana')
print(name_list)

# Clear      remove all the things and gives empty list only
list = [{'name':'sarath'},1,[1,2,3]]
list.clear()
print(list)

# Count     How many times the particular element apperas in list
li = ['a','e','i','o','u','a']
count = li.count('a')
print(count)

# Extend    Modifies the original list
names = ['sarath','bharath']
name = ['vishnu']
names.extend(name)
print(names)

# Index
vowels = ['a','é','i','o','u']
ind = vowels.index('i')
print(ind)

# Insert      it does not return anything it just modifiy the original list only
names = ['sarath','bharath','vishnu']
ins = names.insert(3,'amma')
print(names)

# Pop        Returns the item present at the given index and this item also removed from the list
languages = ['python','java','mule soft','c++']
pop_ele = languages.pop(3)
print(pop_ele)

# Remove    its does not return anything
names = ['sarath','bharath','amma','vishnu']
names.remove('sarath')
print(names)

# Here remove method can remove only first occurence only
names = ['sarath','sarath','bharath','amma','vishnu']
names.remove('sarath')
print(names)

# Reverse
list = [1,2,3]
list.reverse()
print(list)

list = [1,2,3]
rev_li = list[::-1]
print(rev_li)

# Sort
vowels = ['e','a','o','u','i']
vowels.sort()
print(vowels)

vowels = ['e','a','o','u','i']
vowels.sort(reverse=True)
print(vowels)

def elements(ele):
    return ele[1]
random = [(3,3),(2,2),(1,1)]
random.sort(key=elements)
print(random)


# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

def get_name(employee):
    return employee.get('Name')
def get_age(employee):
    return employee.get("age")
def get_salary(employee):
    return employee.get('salary')
employees.sort(key=get_name)
print(employees,end='\n\n')
employees.sort(key=get_age)
print(employees,end='\n')
employees.sort(key=get_salary,reverse=True)
print(employees,end='\n')


# Creating a Dictionary
dict = {'name':'sarath','age':24}
print(dict['name'])

# Updating a dict
dict = {'name':'sarath','age':24}
dict['name']='vishnu'
print(dict)

# Deleting a dict
dict = {'name':'sarath','age':24}
del dict['age']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)

dict = {'name':'sarath','age':24,'name':'vishnu'}
print(type(dict))

# keys
dictionary = {'name':'sarath','age':24,'gender':'male','address':'bangalore'}
print(dictionary.keys())

# values
dictionary = {'name':'sarath','age':24,'gender':'male','address':'bangalore'}
print(dictionary.values())
print(dictionary['name'])

# items
dictionary = {'name':'sarath','age':24,'gender':'male','address':'bangalore'}
new = dictionary.items()
print(type(new))

# update
dictionary = {'name':'sarath','age':24,'gender':'male','address':'bangalore'}
dict = {'age':23}
dictionary.update(dict)
print(dictionary)

# clear
dictionary = {'name':'sarath','age':24,'gender':'male','address':'bangalore'}
dictionary.clear()
print(dictionary)

# fromkeys
keys = {'a','e','o','u','i'}
vowels = dict.fromkeys(keys)
print(vowels)

keys = {'a','e','o','u','i'}
values = 'vowel'
vowels = dict.fromkeys(keys,values)
print(vowels)

# copy
names = {'manvith','sarath','bharath'}
new_copy = names.copy()
print(new_copy)

# get
details = {'name':'sarath','age':24,'location':'bangalore'}
print(details.get('name'))
print(details.get('age'))

