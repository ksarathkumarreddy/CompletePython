'''
Every value in python has a data type.
1.Integer
2.Strings
3.List
4.Tuple
5.Dict
6.Set
7.Frozen Set

'''
# Strings

'''
Strings are created as simple as assign single or double quotes.
'''
str = 'python programming'
print(str)

# string methods

# Capitalize---> First letter must be upper case
str = 'sarath'
capi_str = str.capitalize()
print(capi_str)

#Casefold-----> converts upper case to lower case
str = 'SARATH'
case_str = str.casefold()
print(case_str)

# Center------> Here give space
str = 'sarath is a good boy'
new_str = str.center(23)
print(new_str)

# Count------> how many times the sub string repeat  in str
str = 'python is awesome'
sub_str = str.count('o')
print(sub_str)

# Encode
name = 'sarath'
encod_name = name.encode()
print(encod_name)

# Endswith
txt = 'python is easy to learn,'
res = txt.endswith('learn,')
print(res)

# Expandtabs----> Here give some space
str = 'sarath\tkumar\treddy'
res = str.expandtabs()
print(res)

# find ---> if str present give the at which index or str not present gives index -1
str = 'python is so powerful language'
res = str.find('so')
res1 = str.find('sarath')
print(res)
print(res1)

# Format
print("Hello {}, your in {}".format('sarath',"bangalore."))
print("Hello {name}, your in {age}".format(name='sarath',age=23))
print("Hello {0}, your in {1}".format('sarath','karnataka'))

# format_map
dict = {"name":"sarath","age":23}
print("{name},{age}".format_map(dict))

# index
txt = 'python programing is not diffcult'
res = txt.index('is')
print("At which index 'is'",res)


# isalnum
name = 'sarath24'
print(name.isalnum())
name = '234'
print(name.isalnum())

# isdecimal
num = '234'
print(num.isdecimal())

# isidentifier
str = 'pythonprogramming'
if str.isidentifier() == True:
    print(str,'is a valid identifier')
else:
    print(str,'is not a valid identifier')

# isprintable---> empty str also gives true but new line is not printable gives false
printable = 'python is so powerful'
print(printable.isprintable())
printable = 'python is so powerful\n'
print(printable.isprintable())

# isspace---> empty str or non printable char gives false
str = ' \t'
print(str.isspace())
s = ''
print(s.isspace())

# istitle----> every word first letter must be caps
s = 'Python Gives Energy'
print(s.istitle())

# join
list = ['1','2','3','4']
sep = ','
print(sep.join(list))

tup = ('sarath','bharath','vishnu')
print(sep.join(tup))

names = 'sarath'
name = 'vishnu'
print(name.join(names))

names = {'sarath','vishnu'}
s = '---'
print(s.join(names))

# maketrans
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

# replace
name = 'sarath,bharath'
print(name.replace('bharath','amma'))

song = 'Let it be, let it be, let it be, let it be'
print(song.replace('let', "don't let"))

# rfind
quote = 'Let it be, let it be, let it be'
result = quote.rfind('let it')
print("Substring 'let it':", result)

# split-----> break the string and returns a list of strings.
txt = 'sarath and bharath'
print(txt.split())

# strip----> remove spaces

str = '   sarath   '
print(str.strip())


# swap case
swap = ('sarath')
print(swap.swapcase())




