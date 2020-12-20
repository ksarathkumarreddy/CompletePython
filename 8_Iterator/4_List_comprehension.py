# List comprehension : I can identify in list comprehension it receives a string or a
# (cont) tuple it work on it like a list only.
# normal for loop using
letters = []
for alph in 'sarath':
    letters.append(alph)
print(letters)

# Now list comprehension

# Syntax
#
txt = [letter for letter in 'vishnu']
print(txt)

tup = [char for char in ('sarath.k.vis')]
print(tup)
number = []
num = [val for val in range(0,10) if val % 2 == 0]
number.append(num)
print(number)


# nested if with list comprehension
num_li = [y ** 2 for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_li)

obj = ["Even" if i%2 == 0 else "Odd" for i in range(10)]
print(obj)

tup = (1,2,3,4)
squ = [item * item for item in tup]
print(squ)











