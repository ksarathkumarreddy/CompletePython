data = {101:'sarath',102:'vishnu',103:'amma'}
print(data)
# keys
print(data.keys())

# values
print(data.values())

# items
print(data.items())

# update
data1 = {104:'python'}
data.update(data1)
print(data)


# clear
print(data1.clear())
print(data1)

# fromkeys
keys = {'a','e','i','o','u'}
vowels = dict.fromkeys(keys)
print(vowels)

keys = {'a','e','i','o','u'}
value = 'vowel'
vowels = dict.fromkeys(keys,value)
print(vowels)

# get
data = {101:'sarath',102:'vishnu',103:'amma'}
print(data.get(101))